from django.db import models
from multiselectfield import MultiSelectField

CATEGORY_CHOICES = (
    (1, 'Svenskt'),
    (2, 'Asiatiskt'),
    (3, 'Mexikanskt'),
    (4, 'Spanskt'),
    (5, 'Indiskt')
)

class Recipe(models.Model):
	title = models.CharField(max_length=300)
	categories = MultiSelectField(choices=CATEGORY_CHOICES, default=1)
	def __str__(self):
		return 'Namn'

class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe)
	title = models.CharField(max_length=300)
	def __str__(self):
		return 'Ingrediens'