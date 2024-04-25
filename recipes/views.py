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
                'number': 9,
                'apiKey': SPOONACULAR_API_KEY
            }
            try:
                response = requests.get(endpoint, params=params, timeout=15)
                response.raise_for_status()
                data = response.json()
                results = data.get('results', [])
                context = {
                    'query': query,
                    'recipes': results,
                    'addRecipeInformation': 'true',
                }
                return render(request, 'recipes/recipes_search_results.html', context)
            except requests.RequestException as e:
                return HttpResponse(f"Failed to fetch recipe search results: {e}")
        return HttpResponse("No query provided for recipe search")
    return HttpResponse("Invalid request method")

def recipe_detail(request, recipe_id):
    endpoint = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': SPOONACULAR_API_KEY
    }
    try:
        response = requests.get(endpoint, params=params, timeout=15)
        response.raise_for_status()
        recipe_data = response.json()
        context = {
            'recipe_data': recipe_data
        }
        return render(request, 'recipes/recipe_detail.html', context)
    except requests.RequestException as e:
        return HttpResponse(f"Failed to fetch recipe details: {e}")