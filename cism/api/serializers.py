from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_likes(self, obj):
        queryset = Post.objects.get(id=obj.id).likes.count()
        return queryset
