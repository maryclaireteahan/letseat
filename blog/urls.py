from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.RecipeHome.as_view(), name='home'),
    path('recipes/', views.CategoryListView.as_view(), name='recipes'),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="single_recipe"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('recipe/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('comment_update/<int:id>', views.commentUpdate, name='comment_update'),
    path('comment_delete/<int:id>', views.commentDelete, name='comment_delete'),
    
]
