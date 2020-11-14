from django.urls import path
from.views import one,two

urlpatterns = [
    path('',one.as_view(),name='home'),
    path('api/',two.as_view(),name='home'),
]
