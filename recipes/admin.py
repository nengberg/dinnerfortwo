from django.contrib import admin
from recipes.models import Recipe, Ingredient
from django_summernote.admin import SummernoteModelAdmin
from django.http import HttpResponse
from django.conf.urls import patterns

class IngredientInline(admin.StackedInline):
	model = Ingredient
	extra = 0

class RecipeAdmin(SummernoteModelAdmin):
	inlines = [IngredientInline]

admin.site.register(Recipe, RecipeAdmin)