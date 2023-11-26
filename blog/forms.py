from .models import Comment, Recipe
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('body',)
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields = ['title', 'author', 'ingredients', 'instructions', 'featured_image', 'image_alt', 'category', ]
        




