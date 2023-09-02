from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Room, Review, DoubleRoom, DeluxeRoom, User, RoomDouble, RoomDeluxe, RoomSuperior, JuniorSuite
from the_profile.models import Profile


class RoomListView(ListView):
    template_name = 'room-list-1.html'
    context_object_name = 'rooms'
    model = Room

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        rooms = Room.objects.order_by('-name_room')
        context['rooms'] = rooms
        return context


class DoubleRoomListView(ListView):
    template_name = 'room-details.html'
    context_object_name = 'double_room'
    model = DoubleRoom

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        double_room = DoubleRoom.objects.all()
        context['double_room'] = double_room
        return context


class DeluxeRoomListView(ListView):
    template_name = 'room-details.html'
    context_object_name = 'double_room'
    model = DeluxeRoom

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        deluxe_room = DeluxeRoom.objects.all()
        context['deluxe_room'] = deluxe_room
        return context


class RoomDeluxeListView(ListView):
    template_name = 'room-list-2.html'
    context_object_name = 'room_double'
    model = RoomDeluxe

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        room_deluxe = RoomDeluxe.objects.all()
        context['room_deluxe'] = room_deluxe
        return context



def double_room(request):
    room_double = RoomDouble.objects.all()

    return render(request, 'room-list-2.html', {'room_double': room_double})


# class RoomListView(ListView):
#     template_name = 'room-list-1.html'
#     context_object_name = 'rooms'
#     model = Room
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         rooms = Room.objects.order_by('-name_room')
#         context['rooms'] = rooms
#         return context

class RoomSuperiorLiView(ListView):
    template_name = 'room-list-2.html'
    context_object_name = 'room_superior'
    model = RoomSuperior

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        room_superior = RoomSuperior.objects.all()
        context['room_superior'] = room_superior
        return context


class JuniorSiteView(ListView):
    template_name = 'room-list-2.html'
    context_object_name = 'junior_site'
    model = JuniorSuite

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        junior_site = JuniorSuite.objects.all()
        context['junior_site'] = junior_site
        return context


class RoomDetailView(DetailView):
    template_name = 'room-details.html'
    model = Room
    # queryset = Room.objects.all()

    # context_object_name = 'room'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['room'] = context.get('object')
        return context

    def post(self, request, pk, *args, **kwargs):

        room = get_object_or_404(Room, id=pk)
        reviews = Review.objects.all()
        # profile = Profile.objects.filter(user=request.user)
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.author.profile = self.request.user.id

                form.room = room

                form.save()
                return redirect('part_room:room', pk)

        else:
            form = ReviewForm()
        return render(request, 'room-details.html', {'reviews': reviews, 'form': form,
                                                     'room': room})


def review_delete(request, id):
    review = Review.objects.get(id=id)
    if review.author.review_author == request.user:
        review.is_removed = True
        review.delete()
    else:
        return HttpResponse("You can not delete other people's commentary!")

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
