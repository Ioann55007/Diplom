from the_profile.models import Profile

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import CommentForm
from .models import NewPost, Comment


class NewsOneView(ListView):
    template_name = 'news-1.html'
    context_object_name = 'posts'
    model = NewPost
    paginate_by = 1


def news_detail(request, slug):
    """Вывод полной статьи
    """
    pagination_by = 2
    post = get_object_or_404(NewPost, slug=slug)
    comments = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = Profile.objects.get(user=request.user)
            form.new_post = post
            form.save()
            return redirect('part_post:news-post', slug)

    else:
        form = CommentForm()
    return render(request, "news-post.html",
                  {"post": post,
                   "comments": comments,
                   "pagination": pagination_by,
                   "form": form})


def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    if comment.user == Profile.objects.get(user=request.user):
        comment.is_removed = True
        comment.delete()
    else:
        return HttpResponse("You can not delete other people's commentary!")

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
