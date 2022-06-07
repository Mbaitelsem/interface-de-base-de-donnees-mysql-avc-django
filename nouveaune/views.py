from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, request

from .models import Enfant, Parent, Fonctionnaire

from .forms import EnfantForm, FonctionnaireForm, ParentForm



def formation_view(request):
    nouveaunes = Enfant.objects.all()
    return render(request, 'nouveaune/list.html', {'nouveaunes': nouveaunes})

def load_form(request):
    form = EnfantForm
    formP = ParentForm
    formF = FonctionnaireForm
    return render(request, 'nouveaune/form.html', {'form': form,'formP': formP, 'formF':formF})

def add_enfant(request):
    
    formF = FonctionnaireForm(request.POST)
    formF.save()
    formP = ParentForm(request.POST)
    formP.save()

    

   
    #if form.is_valid():
    p = Parent.objects.all().last()
    lastIDparent = p.id

    f = Fonctionnaire.objects.all().last()
    lastIDfonctionnaire = f.id
    #print(lastIDparent)

    #formE = EnfantForm(request.POST)
    #formE.cleaned_data.get("nom")

   # Enfant.objects.create(
   #     nom = formE.cleaned_data.get("nom"),
   #     prenom = formE.cleaned_data.get("nom"),
    #    sexe = formE.cleaned_data.get("sexe"),
    #    lieu_naissance = formE.cleaned_data.get("lieu_naissance"), 
    #    date_naissance = formE.cleaned_data.get("anne_naissance"),
   #     anne_naissance = formE.cleaned_data.get("sexe"),
    #    fonctionnaire_id = lastIDfonctionnaire,
   #     parent_id = lastIDparent,
   #     )
   
    

    #formE.save()
    return HttpResponse(formF.cleaned_data.all().last())


def detail_enfant(request, id):
    enfant = Enfant.objects.get(id=id)
    return render(request, 'nouveaune/detail_enfant.html', {'enfant': enfant})
