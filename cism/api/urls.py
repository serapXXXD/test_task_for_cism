from .views import PostListAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('post/create/', PostCreateAPIView.as_view()),
    path('post/update/<int:pk>/', PostUpdateAPIView.as_view()),
    path('post/delete/<int:pk>/', PostDeleteAPIView.as_view()),
]
