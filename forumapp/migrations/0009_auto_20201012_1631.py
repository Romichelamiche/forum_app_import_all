# Generated by Django 3.0.7 on 2020-10-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0008_auto_20201012_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='user_123', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user_123', max_length=255),
            preserve_default=False,
        ),
    ]