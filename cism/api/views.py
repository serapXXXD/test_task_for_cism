from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from blog.models import Post, Like


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['POST'], permission_classes=[IsAuthenticated], detail=True)
    def like(self, request, pk):
        like, created = Like.objects.get_or_create(liker=request.user, liked_post=get_object_or_404(Post, pk=pk))
        likes = like.liked_post.likes.count()
        if created:
            return Response({'likes': likes}, status=status.HTTP_201_CREATED)

        like.delete()
        likes = like.liked_post.likes.count()
        return Response({'likes': likes}, status=status.HTTP_200_OK)
