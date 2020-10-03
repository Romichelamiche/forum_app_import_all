from django import forms
from forumapp.models import Probleme, Commentaire
from bootstrap_datepicker_plus import DatePickerInput


class ProblemeForm(forms.ModelForm):

    class Meta:
        model = Probleme
        fields = ['titre_probleme', 'desc_probleme', 'membre_createur_probleme', 'date_publicaiton', 'resolu_probleme', 'commentaire_probleme']
        widgets = {
            'titre_probleme' : forms.TextInput(attrs={'class':'form-control'}),
            'desc_probleme' : forms.Textarea(attrs={'class':'form-control', 'size' : 40}),
            'membre_createur_probleme' : forms.Select(attrs={'class':'form-control'}),
            'date_publicaiton': DatePickerInput(attrs={'data-target':'#datetimepicker1'}),
            'commentaire_probleme' : forms.Textarea(attrs={'class':'form-control', 'size' : 40})

        }

class CommentaireForm(forms.ModelForm):

    class Meta:
        model = Commentaire
        fields = ['commentaire',]

        widgets = {
            'commentaire' : forms.Textarea(attrs={'class':'form-control'}),
        }








