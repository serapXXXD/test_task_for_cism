# Generated by Django 5.0 on 2023-12-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_like_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_like',
            field=models.BooleanField(default=True),
        ),
    ]