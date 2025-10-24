from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer


# Ingredient CRUD
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# Recipe CRUD
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# Suggest recipes based on available ingredients
@api_view(['GET'])
def suggest_recipes(request):
    ingredients = Ingredient.objects.all()
    available_ingredient_names = [i.name.lower() for i in ingredients]

    possible_recipes = []
    for recipe in Recipe.objects.all():
        recipe_ingredients = [i.name.lower() for i in recipe.ingredients.all()]
        if all(i in available_ingredient_names for i in recipe_ingredients):
            possible_recipes.append(recipe)

    serializer = RecipeSerializer(possible_recipes, many=True)
    return Response(serializer.data)
