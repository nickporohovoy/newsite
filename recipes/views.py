from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

def home(request):
    recipes = Recipe.objects.all()[:5]  # 5 рецептов
    return render(request, 'recipes/home.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)  # Если форма была отправлена
        if form.is_valid():
            form.save()  # Сохраняем рецепт в базу данных
            return redirect('home')  # Переадресация на главную страницу после успешного сохранения
    else:
        form = RecipeForm()  # Создаем пустую форму

    return render(request, 'recipes/add_recipe.html', {'form': form})
