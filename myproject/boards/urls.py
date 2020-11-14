from django.urls import path
from .views import aos

urlpatterns = [
    path('',aos.as_view(),name='home'),
    
]
