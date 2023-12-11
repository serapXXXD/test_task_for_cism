from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.CharField(max_length=255, verbose_name='Автор поста')
    topic = models.CharField(max_length=255, verbose_name='Тема поста')
    body = models.TextField(verbose_name='Содержимое поста')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'{self.author}, {self.topic}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-id']


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        constraints = [models.UniqueConstraint(fields=['liker', 'liked_post'], name='unique_together_liker_post')]
