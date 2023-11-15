from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.RecipeHome.as_view(), name='home'),
    path('recipes/', views.CategoryListView.as_view(), name='recipes'),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="single_recipe"),
    path('recipe/<slug:slug>/like/', views.RecipeLike.as_view(), name='recipe_like'),
]
