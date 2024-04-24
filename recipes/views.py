from django.shortcuts import render, HttpResponse
import os
import requests
# Create your views here.

def recipe_search(request):
    return render(request, 'recipes/recipe_search.html')

def recipe_search_results(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        return render(request, 'recipes/recipes_search_results.html', context={'query':query})