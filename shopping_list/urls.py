from django.urls import path

from .views import HomeView, RecipeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/', RecipeView.as_view(), name='recipe')
]
