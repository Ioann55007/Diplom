from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Room, Images


class RoomListView(ListView):
    template_name = 'room-list-1.html'
    context_object_name = 'rooms'
    model = Room

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        rooms = Room.objects.order_by('-name_room')
        context['rooms'] = rooms
        return context





class RoomDetailView(DetailView):
    template_name = 'room-details.html'
    model = Room
    queryset = Room.objects.all()
    # context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['room'] = context.get('object')
        images = Images.image.all()
        context['images'] = images
        return context


    # def post(self, request):
    #     room = Room.objects.all()
    #     image_list = room.several_image.all()
    #     return render(request, 'room-details.html', {'images': image_list})


