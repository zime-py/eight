from django.contrib import admin
from . models import post#,tost,gost


class fig(admin.ModelAdmin):
    list_filter=('created','name',)
    search_fields = ("name",)
    list_display = ("name","roll", )

#class AdminView():

admin.site.register(post,fig)
#admin.site.register(tost)
#admin.site.register(gost)