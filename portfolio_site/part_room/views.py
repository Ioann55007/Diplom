from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Room, Review, DoubleRoom, DeluxeRoom, SuperiorRoom
from base_one.models import BookingHotel

from base_one.forms import BookingForm

from the_profile.models import Profile


class RoomListView(ListView):
    model = Room
    queryset = Room.objects.all()
    template_name = 'room-list-1.html'
    context_object_name = "rooms"
    paginate_by = 1


class SuperiorRoomListView(ListView):
    template_name = 'room-details.html'
    model = SuperiorRoom



class SuperiorDetailView(DetailView):
    template_name = "superior.html"
    model = SuperiorRoom
    context_object_name = "room"


class DoubleRoomListView(ListView):
    template_name = 'room-details.html'
    context_object_name = 'double_room'
    model = DoubleRoom

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        double_room = DoubleRoom.objects.all()
        context['double_room'] = double_room
        return context


class DoubleRoomDetailView(DetailView):
    template_name = "double.html"
    model = DoubleRoom
    context_object_name = "room"


class DeluxeRoomListView(ListView):
    template_name = 'room-details.html'
    model = DeluxeRoom




class DeluxeRoomDetailView(DetailView):
    template_name = "deluxe.html"
    model = DeluxeRoom
    context_object_name = "room"




def room_detail(request, pk):
    room = get_object_or_404(Room, id=pk)
    bookings = BookingHotel.objects.all()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # form.user = Profile.objects.get(user=request.user)
            form.user_booking = Profile.objects.get(user=request.user)
            form.room = room
            form.price = room.price
            form.save()
            return redirect('booking')

    else:
        form = BookingForm()
    return render(request, "room-details.html",
                  {"room": room,
                   "bookings": bookings,
                   "form": form})


def review_room(request, pk):
    room = get_object_or_404(Room, id=pk)
    reviews = Review.objects.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = Profile.objects.get(user=request.user)
            form.room = room
            form.save()
            return redirect('part_room:room', pk)

    else:
        form = ReviewForm()
    return render(request, "room-details.html",
                  {"room": room,
                   "reviews": reviews,
                   "form": form})


def review_delete(request, id):
    review = Review.objects.get(id=id)
    if review.author == Profile.objects.get(user=request.user):
        review.is_removed = True
        review.delete()
    else:
        return HttpResponse("You can not delete other people's commentary!")

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
