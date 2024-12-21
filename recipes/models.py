from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)  # Название рецепта
    description = models.TextField()  # Описание
    steps = models.TextField()  # Шаги приготовления
    cooking_time = models.PositiveIntegerField()  # Время приготовления (в минутах)
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)  # Изображение
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор (связь с пользователем)

    def __str__(self):
        return self.title
