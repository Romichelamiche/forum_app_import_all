# Generated by Django 3.0.7 on 2020-10-14 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0009_auto_20201012_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
