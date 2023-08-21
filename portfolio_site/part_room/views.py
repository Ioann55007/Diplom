# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
#
# # from .forms import ReviewForm
# # from .models import Room, Review
#
#
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
#
#
#
#
#
# class RoomDetailView(DetailView):
#     template_name = 'room-details.html'
#     model = Room
#     queryset = Room.objects.all()
#     # context_object_name = 'room'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['room'] = context.get('object')
#         return context
#
#
#     def post(self, request, pk):
#         review_list = Review.objects.all()
#         if request.method == 'POST':
#             form_review = ReviewForm(request.POST)
#             if form_review.is_valid():
#                 form_review = form_review.save(commit=False)
#                 form_review.author = self.request.user
#                 form_review.save()
#                 return redirect('room-detail', pk)
#
#         else:
#             form_review = ReviewForm()
#         return render('room-details.html', {'review_list': review_list, 'form_review': form_review})
#
