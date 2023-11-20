from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.views import generic, View
from requests import post
from .models import Recipe, Category, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm

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
        comments = recipe.comments.filter(approved=True).order_by('-created_on')
        liked = False
        context = {
            'recipe': recipe,
            'comments': comments,
            'commented': False,
            'liked': liked,
            'comment_form': CommentForm(),
        }
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render (request,'single_recipe.html',context)
        
        
    def post(self, request, slug, *args, **kwargs):
        queryset= Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment.user = request.user
            comment.post = recipe
            comment.save()
        else:
            comment_form = CommentForm()
        
        return render (
            request,
            'single_recipe.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
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
            
    
@login_required
def commentUpdate(request, id):  
    comment_instance = get_object_or_404(Comment, id=id)
    form = CommentForm(initial={'Comment': Comment.body})
    if comment_instance.user == request.user:

        if request.method == "POST":  
            form = CommentForm(request.POST, instance=comment_instance)  
            if form.is_valid():  
                try:  
                    form.save() 
                    return redirect('/recipes')  
                except Exception as e: 
                    pass    
        return render(request,'comment_update.html',{'form':form})  
    else:
    # Redirect or show a message indicating the user doesn't have permission to edit
        return HttpResponse("You do not have permission to edit this comment.")

@login_required
def commentDelete(request, id):
    comment_instance = get_object_or_404(Comment, id=id)

    if comment_instance.user == request.user:
        if request.method == 'POST':
            comment_instance.delete()
            return redirect('/recipes')  # Redirect to appropriate page after deletion
        else:
            # Optionally, handle confirmation in a template
            return render(request, 'comment_delete.html', {'comment_instance': comment_instance})
    else:
        # Redirect or show a message indicating the user doesn't have permission to delete
        return HttpResponse("You do not have permission to delete this comment.")