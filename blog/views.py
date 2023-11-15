from django.shortcuts import render, get_object_or_404, reverse

from django.views import generic, View
from .models import Recipe, Category
from django.http import HttpResponseRedirect
class RecipeHome(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    
class RecipeList(generic.ListView):
    model = Recipe
    queryset= Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'all_recipes.html'
    paginate_by = 6

class RecipeDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset= Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render (
            request,
            'single_recipe.html',
            {
                'recipe': recipe,
                'comments': comments,
                'liked': liked
            },
        )
        
        
        
class CategoryListView(generic.ListView):
    model = Category
    template_name='all_recipes.html'
    context_object_name = 'categories'
    
    

class RecipeLike(View):
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
            
