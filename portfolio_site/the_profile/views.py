from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, DetailView, UpdateView

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import EmailVerification, Profile
from part_room.models import User
from django.contrib.auth.decorators import login_required



class DeleteProfile(DeleteView):
    model = Profile
    success_url = reverse_lazy("index")


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active and user.is_verify_email:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Подтвердите регистрацию по почте')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'register.html', context)


# @login_required(login_url='/users/login/')
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user)
#     context = {
#         'title': 'profile',
#         'form': form,
#     }
#     return render(request, 'profile.html', context)

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    form_class = UserProfileForm

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data()
        # profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        profile = Profile.objects.get(user=self.request.user)


        context["profiles"] = profile
        return context


# class ProfileApi(APIView):
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Метод PUT не разрешён"})
#
#         try:
#             instance = Profile.objects.get(pk=pk)
#         except:
#             return Response({"error": "Объект не найден"})
#
#         serializer = ProfileSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'profile_form.html'

    def get_success_url(self):
        return reverse('profile', kwargs={"pk": self.object.id})


# @login_required(login_url='/users/login/')
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             profile = Profile.objects.get(user=request.user)
#
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user)
#     context = {
#         'title': 'Profile',
#         'form': form,
#     }
#     return render(request, 'profile.html', context)




def logout(request):
    auth.logout(request)
    return redirect('index')


class EmailVirificationView(TemplateView):
    template_name = "email_verification.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "email confirmation"
        return context

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verify_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return redirect('index')
