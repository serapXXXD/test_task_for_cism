from django.urls import path
from .views import IndexView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, post_like

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/like/', post_like, name='like')
]
