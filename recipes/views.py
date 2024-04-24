from django.shortcuts import render, HttpResponse
import os
import requests
# Create your views here.

SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')

def recipe_search(request):
    return render(request, 'recipes/recipe_search.html')

def recipe_search_results(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            endpoint = 'https://api.spoonacular.com/recipes/complexSearch'
            params = {
                'query': query,
                'number': 10,
                'apiKey': SPOONACULAR_API_KEY
            }
            
            response = requests.get(endpoint, params=params)
            if response.status_code == 200:
                data = response.json()
                results = data.get('results', [])
                context = {
                    'query': query,
                    'recipes': results
                }
                return render(request, 'recipes/recipes_search_results.html', context)

            else:
                return HttpResponse("Failed to fetch recipe search results")
        else:
            return HttpResponse("No query provided for recipe search")
    else:
        return HttpResponse("Invalid request method")