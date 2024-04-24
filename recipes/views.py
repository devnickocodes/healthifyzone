from django.shortcuts import render

# Create your views here.


def recipe_search(request):
    return render(request, 'recipes/recipe_search.html')