# Generated by Django 3.1.3 on 2020-12-22 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
    ]