from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, DetailView, UpdateView

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages

from django.views.generic.base import TemplateView
from .models import EmailVerification, Profile
from part_room.models import User


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


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'profile_form.html'

    def get_success_url(self):
        return reverse('profile', kwargs={"pk": self.object.id})


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
