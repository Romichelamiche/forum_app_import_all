# Generated by Django 3.0.7 on 2020-10-18 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0010_remove_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]