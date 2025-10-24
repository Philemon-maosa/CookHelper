from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")

    def __str__(self):
        return self.name