# Generated by Django 3.1.3 on 2020-12-24 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_auto_20201224_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
    ]
