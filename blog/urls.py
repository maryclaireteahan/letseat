from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeHome.as_view(), name='home'),
    path('/recipes', views.RecipeList.as_view(), name='recipes'),

]