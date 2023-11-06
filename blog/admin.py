from turtle import clear
from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

""" 
Register Post model and PostAdmin class to admin site
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

