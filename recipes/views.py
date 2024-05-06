from django.shortcuts import render, HttpResponse
import os
import requests
# Create your views here.

SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')


def recipe_search(request):
    """
    Render the page for searching recipes.

    **Template:**

    :template:`recipes/recipe_search.html`
    """
    return render(request, 'recipes/recipe_search.html')


def recipe_search_results(request):
    """
    Fetch and display the search results for recipes.

    **Context**

    ``query``
        The search query provided by the user.

    ``recipes``
        A list of recipe search results.

    **Template:**

    :template:`recipes/recipes_search_results.html`
    """
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
                return render(request, 'recipes/recipes_search_results.html',
                              context)
            except requests.RequestException as e:
                return HttpResponse(f"Failed to fetch recipe \
                search results: {e}")
        return HttpResponse("No query provided for recipe search")
    return HttpResponse("Invalid request method")


def recipe_detail_with_instructions(request, recipe_id):
    """
    Fetch and display the details of a recipe along with its instructions.

    **Context**

    ``recipe_data``
        Details of the recipe fetched from Spoonacular API.

    ``instructions_data``
        Instructions for preparing the recipe fetched from Spoonacular API.

    **Template:**

    :template:`recipes/recipe_detail.html`
    """
    detail_endpoint = (
                f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    )
    detail_params = {
        'apiKey': SPOONACULAR_API_KEY
    }

    instructions_endpoint = (
        f'https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions'
    )
    instructions_params = {
        'apiKey': SPOONACULAR_API_KEY
    }
    try:
        detail_response = requests.get(detail_endpoint,
                                       params=detail_params, timeout=10)
        detail_response.raise_for_status()
        recipe_data = detail_response.json()

        instructions_response = requests.get(instructions_endpoint,
                                             params=instructions_params,
                                             timeout=10)
        instructions_response.raise_for_status()
        instructions_data = instructions_response.json()

        context = {
            'recipe_data': recipe_data,
            'instructions_data': instructions_data
        }
        return render(request, 'recipes/recipe_detail.html', context)
    except requests.RequestException as e:
        return HttpResponse(f"Failed to fetch recipe details: {e}")
