from .models import Like


def like_post(post, user):
    like, created = Like.objects.get_or_create(liker=user, liked_post=post)
    if not created:
        like.delete()
    return post.likes.count(), created
