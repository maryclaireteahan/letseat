from . import views
from django.urls import path
from django.urls import path, handler404

urlpatterns = [
    path('', views.RecipeHome.as_view(), name='home'),
    path('recipes/', views.CategoryListView.as_view(),
         name='recipes'),
    path("<slug:slug>/", views.RecipeDetail.as_view(),
         name="single_recipe"),
    path('like/<slug:slug>', views.RecipeLike.as_view(),
         name='recipe_like'),
    path('recipe/<slug:slug>/', views.RecipeDetail.as_view(),
         name='recipe_detail'),
    path('comment_edit/<int:id>', views.commentEdit,
         name='comment_edit'),
    path('comment_delete/<int:id>', views.commentDelete,
         name='comment_delete'),
    path('recipes/create/', views.RecipeCreate.as_view(),
         name='recipe_create'),
    path('admin_recipe_edit/<int:id>', views.recipeEdit,
         name='recipe_edit'),
    path('admin_recipe_delete/<int:id>', views.recipeDelete,
         name='recipe_delete'),
]

handler404 = 'letseat.views.commentEdit'