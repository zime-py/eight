from django.contrib import admin
from .models import Board, Topic, Post, Lost

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Lost)