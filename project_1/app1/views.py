from django.shortcuts import render #*
from django.views.generic import ListView
from.models import CustomUser #*

class lol(ListView):
    template_name='home.html'
    model=CustomUser
