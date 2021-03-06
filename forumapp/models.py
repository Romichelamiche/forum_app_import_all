from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, Group, User )
from django.http import HttpRequest as request
from django.contrib.auth.middleware import AuthenticationMiddleware


class Favorite(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    sujet = models.ForeignKey('Probleme', unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.sujet


class Membre(models.Model):
    nom_membre = models.CharField(max_length=200)
    prenom_membre = models.CharField(max_length=400)
    email_membre = models.EmailField()
    date_inscription_membre = models.DateField()
    login_membre = models.CharField(max_length=200)
    password_membre = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_membre

class Solution(models.Model):
    probleme_solution = models.ForeignKey('Probleme', on_delete=models.CASCADE)
    titre_solution = models.CharField(max_length=200)
    desc_solution = models.TextField()
    piece_jointe_solution = models.FileField()

    def __str__(self):
        return self.titre_solution


class Probleme(models.Model):
    titre_probleme = models.CharField(max_length=200)
    desc_probleme = models.TextField(verbose_name='Description')
    resolu_probleme = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='probleme_created_by')

    def __str__(self):
        return self.titre_probleme

class Commentaire(models.Model):
    commentaire = models.TextField(verbose_name='Commentaire')
    probleme = models.ForeignKey(Probleme, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.commentaire


