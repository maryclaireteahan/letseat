from django.contrib import admin
from .models import Recipe, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Register Recipe model and RecipeAdmin class to admin site
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'category')
    summernote_fields = ('ingredients', 'instructions')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Register Comment model and CommentAdmin class to admin site
    """
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on', )
    search_fields = ('name', 'email', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Register Category model and CategoryAdmin class to admin site
    """
    prepopulated_fields = {'slug': ('name',)}
