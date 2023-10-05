from .forms import ReviewForm


def room_form(request):
    return {'room_form': ReviewForm}