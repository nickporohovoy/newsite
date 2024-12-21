from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cooking_time')  # Поля, которые будут видны в списке
    search_fields = ('title', 'description')  # Поля для поиска
    list_filter = ('author',)  # Фильтры в админке
