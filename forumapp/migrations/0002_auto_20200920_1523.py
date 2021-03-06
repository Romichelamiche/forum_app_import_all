# Generated by Django 3.0.7 on 2020-09-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='probleme',
            name='commentaire_probleme',
            field=models.TextField(null=True, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='date_publicaiton',
            field=models.DateField(verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='desc_probleme',
            field=models.TextField(verbose_name='Description'),
        ),
    ]
