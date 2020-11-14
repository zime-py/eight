from django.views.generic import ListView
from .models import Do, Did, Done, Go

class aos(ListView):
    model = Go
    template_name = 'home.html'
    context_object_name='boards'
