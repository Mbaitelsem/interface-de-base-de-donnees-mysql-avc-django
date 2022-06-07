from django import forms
from django.db import models
from django.forms import fields
from .models import Enfant, Fonctionnaire, Parent

#from django.forms import modelform_factory
#from myapp.models import Book
#BookForm = modelform_factory(Book, fields=("author", "title"))

class EnfantForm(forms.ModelForm):

#class NameForm(forms.Form):
    nom = forms.CharField(label='nom', max_length=100)
    prenom = forms.CharField(label='prenom', max_length=100)
    sexe = forms.CharField(label='sexe', max_length=100)
    lieu_naissance = forms.CharField(label='lieu_naissance', max_length=100)
    date_naissance = forms.DateField()
    annee_naissance = forms.CharField()
    

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields =  fields = {'nom', 'prenom', 'sexe', 'fonction', 'situation_matrimoniale'}
        widget = {
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'sexe': forms.TextInput(attrs={'class':'form-control'}),
            'fonction': forms.TextInput(attrs={'class':'form-control'}),
            'situation_matrimoniale': forms.TextInput(attrs={'class':'form-control'})
        }


class FonctionnaireForm(forms.ModelForm):
    class Meta:
        model = Fonctionnaire
        fields = {'nom', 'prenom', 'login'}
        widget = {
            'nom' : forms.TextInput(attrs={'class':'form-control'}),
            'prenom' : forms.TextInput(attrs={'class':'form-control'}),
            'login' : forms.TextInput(attrs={'class':'form-control'}),
            
        }