from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from meals.views import IngredientViewSet, suggest_recipes

router = routers.DefaultRouter()
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/suggestions/', suggest_recipes),
]
