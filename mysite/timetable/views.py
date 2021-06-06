from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TimeTable
from django.views.generic.list import ListView
 
# получение данных из бд




class PlacesView(ListView):
    model = TimeTable
    template_name = 'foodplaces.html'
    context_object_name = 'places'