from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from meals.views import IngredientViewSet, RecipeViewSet, suggest_recipes

router = routers.DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/suggest/', suggest_recipes, name='suggest_recipes'),
]
