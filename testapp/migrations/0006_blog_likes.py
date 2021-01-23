# Generated by Django 3.1.3 on 2020-12-22 13:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0005_remove_blog_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='BlogLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
