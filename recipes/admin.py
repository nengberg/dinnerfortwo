from django.contrib import admin
from recipes.models import Recipe, Ingredient
from django_summernote.admin import SummernoteModelAdmin

class IngredientInline(admin.StackedInline):
	model = Ingredient
	extra = 1

class RecipeAdmin(admin.ModelAdmin):
	inlines = [IngredientInline]
		
class SomeModelAdmin(SummernoteModelAdmin):
	pass


admin.site.register(Recipe, RecipeAdmin)