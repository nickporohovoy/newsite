# from django.db import models

# # Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.IntegerField(help_text="Укажите время в минутах")
    image = models.ImageField(upload_to='recipes/images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
