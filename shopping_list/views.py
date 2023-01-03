from django.views.generic import FormView, TemplateView

from .forms import RecipeSearchForm


class HomeView(FormView):
    template_name = 'home.html'
    form_class = RecipeSearchForm
    success_url = '/recipe/'


class RecipeView(TemplateView):
    template_name = 'recipe_ranking.html'
