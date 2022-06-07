from django.db import models
from django.db.models.base import Model

# Create your models here.
class Parent(models.Model):
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    sexe = models.CharField(max_length=60)
    fonction = models.CharField(max_length=60)
    situation_matrimoniale = models.CharField(max_length=60)
    def __str__(self):
        return self.nom

class Fonctionnaire(models.Model):
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    login = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    def __str__(self):
        return self.nom

class Enfant(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)
    fonctionnaire = models.ForeignKey(Fonctionnaire, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    sexe = models.CharField(max_length=60)
    lieu_naissance = models.CharField(max_length=60)
    date_naissance = models.DateField(default ="")
    annee_naissance = models.CharField(max_length=60)
    def __str__(self):
        return self.nom







   
