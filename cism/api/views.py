from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from blog.models import Post, Like
from blog.utils import like_post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=['POST'], permission_classes=[IsAuthenticated], detail=True)
    def like(self, request, pk):
        post = self.get_object()
        like_count, created = like_post(post, request.user)
        if not created:
            return Response({'likes': like_count}, status=status.HTTP_200_OK)
        return Response({'likes': like_count}, status=status.HTTP_201_CREATED)
