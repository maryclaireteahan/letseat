from turtle import clear
from django.contrib import admin
from .models import Recipe, Comment, Category
from django_summernote.admin import SummernoteModelAdmin

""" 
Register Recipe model and RecipeAdmin class to admin site
"""
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    prepopulated_fields= {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'category')
    summernote_fields = ('ingredients','instructions')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    
""" 
Register Comment model and CommentAdmin class to admin site
"""
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

""" 
Register Category model and CategoryAdmin class to admin site
"""
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):   
    prepopulated_fields= {'slug': ('name',)}


