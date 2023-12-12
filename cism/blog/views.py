from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from .forms import PostForm


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post_id = self.request.path.split('/')[-2]
        context['is_like'] = Like.objects.filter(liked_post_id=post_id).filter(liker_id=self.request.user.id).exists()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('blog:index')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('blog:index')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog:index')


@login_required(login_url='/api/v1/auth/users/')
def post_like(request, pk):
    like, created = Like.objects.get_or_create(liker=request.user, liked_post=get_object_or_404(Post, pk=pk))
    if created:
        return redirect(f'/post/{pk}')
    like.delete()
    return redirect(f'/post/{pk}')
