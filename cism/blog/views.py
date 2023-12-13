from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .utils import like_post
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
        post = self.get_object()
        context['is_like'] = Like.objects.filter(liked_post=post).filter(liker=self.request.user).exists()
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
    post = get_object_or_404(Post, id=pk)
    like_post(post, request.user)
    return redirect(f'/post/{pk}/')
