# Generated by Django 3.0.7 on 2020-09-21 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0003_auto_20200921_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentaire', models.TextField(verbose_name='Commentaire')),
                ('probleme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumapp.Probleme')),
            ],
        ),
    ]
