from django.db import models

class Recipe(models.Model):
	title = models.CharField(max_length=300)
	def __str__(self):
		return 'Namn'

class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe)
	title = models.CharField(max_length=300)
	def __str__(self):
		return 'Ingrediens'