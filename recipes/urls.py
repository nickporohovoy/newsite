from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
]
