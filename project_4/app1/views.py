#from django.shortcuts import render
from django.views.generic import ListView
from.models import cool
from rest_framework import generics
from .serializers import sos


class one(ListView):
    template_name='home.html'
    model=cool
    
class two(generics.ListAPIView):
    queryset = cool.objects.all()
    serializer_class = sos
