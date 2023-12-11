from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'topic', 'body', 'pub_date')


admin.site.register(Post, PostAdmin)
