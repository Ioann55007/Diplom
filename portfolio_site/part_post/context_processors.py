from .forms import CommentForm


def my_form(request):
    return {'my_form': CommentForm}