from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from recipes.models import Recipe

def index(request):
    return render(request, 'recipes/index.html')

def detail(request, recipe_id):
	try:
		recipe = Recipe.objects.get(pk=recipe_id)
	except Recipe.DoesNotExist:
		raise Http404
		return render(request, 'polls/detail.html', {'recipe': recipe})

def new(request):
	return HttpResponse("Skapa nytt recept")