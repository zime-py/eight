from django.urls import path,re_path
from .views import sos,cos

urlpatterns = [
#path('',sos.as_view(),name='home'),
re_path(( r'\d+/[a-z]+/\d+'), sos.as_view(),name='home'),
#re_path(( r'\d+/[a-z A-Z]+/\d+'), cos.as_view(),name='base'),
re_path(( r'book/<int:pk>'), cos.as_view(),name='base'),
#re_path(( r'^love/w/w/w/lami$'), cos.as_view(),name='base'),
]
