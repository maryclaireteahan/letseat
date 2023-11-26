from .models import Comment, Recipe
from django import forms

class CommentForm(forms.ModelForm):
    """
    Form for commenting on single recipes
    """
    class Meta:
        model=Comment
        fields = ('body',)
        
class RecipeForm(forms.ModelForm):
    """
    Form for creating on single recipes on the frontend
    """
    class Meta:
        model=Recipe
        fields = ['title', 'author', 'ingredients', 'instructions', 'featured_image', 'image_alt', 'category', ]
        




