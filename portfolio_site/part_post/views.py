from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from .form import CommentForm
from .models import NewPost, Comment


class NewsOneView(ListView):
    template_name = 'news-1.html'
    context_object_name = 'posts'
    model = NewPost



class NewsDetail(DetailView):
    template_name = 'news-post.html'
    model = NewPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['post'] = context.get('object')
        return context

    def post(self, request, slug=None, *args, **kwargs):

        new_post = get_object_or_404(NewPost, slug=slug)
        comments = Comment.objects.all()
        # profile = Profile.objects.filter(user=request.user)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user.user = self.request.user.id

                form.new_post = new_post

                form.save()
                return redirect('part_post:news-post', slug)

        else:
            form = CommentForm()
        return render(request, 'news-post.html', {'comments': comments, 'form': form,
                                                     'new_post': new_post})


