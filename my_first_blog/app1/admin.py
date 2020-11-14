#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import post,most

admin.site.register(post)
admin.site.register(most)
