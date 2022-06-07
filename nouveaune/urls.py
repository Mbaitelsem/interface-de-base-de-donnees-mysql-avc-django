from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.formation_view, name='nouveaunes'),
    path('form', views.load_form, name='ajout_nouveaune'), 
    path('add_enfant', views.add_enfant),
    path('detail_enfant/<int:id>', views.detail_enfant)
]
