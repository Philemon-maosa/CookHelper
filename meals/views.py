from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer
from rest_framework import viewsets
from .models import Ingredient
from .serializers import IngredientSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


@api_view(['GET'])
def suggest_recipes(request):
    # Get all user ingredients
    user_ingredients = Ingredient.objects.values_list('name', flat=True)
    user_ingredients = [name.lower() for name in user_ingredients]

    # Get all recipes
    recipes = Recipe.objects.all()
    possible_recipes = []

    for recipe in recipes:
        recipe_ingredients = [i.name.lower() for i in recipe.ingredients.all()]
        # If user has all required ingredients
        if all(i in user_ingredients for i in recipe_ingredients):
            possible_recipes.append(recipe)

    serializer = RecipeSerializer(possible_recipes, many=True)
    return Response(serializer.data)
