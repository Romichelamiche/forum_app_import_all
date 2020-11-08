from django import forms
from django.contrib.auth.forms import UserCreationForm
from forumapp.models import Probleme, Commentaire
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput


class ProblemeForm(forms.ModelForm):

    class Meta:
        model = Probleme
        fields = ['titre_probleme', 'desc_probleme', 'resolu_probleme']
        widgets = {
            'titre_probleme' : forms.TextInput(attrs={'class':'form-control'}),
            'desc_probleme' : forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentaireForm(forms.ModelForm):

    class Meta:
        model = Commentaire
        fields = ['commentaire',]

        widgets = {
            'commentaire' : forms.Textarea(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm): #We start from a model already implemented by django which is not located in models.py file as well as the UserCreationForm which is not a personal model but an already set one by django automatically
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmation mot de passe'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']










