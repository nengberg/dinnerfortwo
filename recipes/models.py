from django import forms
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
	title = models.CharField(max_length=300, verbose_name='Namn')
	categories = MultiSelectField(choices=CATEGORY_CHOICES, default=1, verbose_name='Kategorier')
	image = models.ImageField(upload_to='pictures/', null=True, verbose_name='Bild')
	description = models.TextField(default='', verbose_name='Instruktioner')
	def __str__(self):
		return self.title

class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe)
	quantity = models.CharField(max_length=300)
	name = models.CharField(max_length=300,default='')
	def __str__(self):
		return 'Ingrediens'


class RecipeForm(forms.ModelForm):

	class Meta:
		model = Recipe
		fields = ['title', 'categories', 'description']
		title = forms.CharField(label='Your name')

class RecipeForm(forms.ModelForm):
	title = forms.CharField(widget=forms.Textarea)