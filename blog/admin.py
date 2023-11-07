from turtle import clear
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

""" 
Register Post model and PostAdmin class to admin site
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields= {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    

""" 
Register Comment model and CommentAdmin class to admin site
"""
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    