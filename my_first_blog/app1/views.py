#from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import post, most

class sos(ListView):
    model = post
    template_name = 'home.html'
    context_object_name='app1'

class cos(ListView):
    model = most
    template_name = 'base.html'
    context_object_name='app1'


