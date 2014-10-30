from django.conf.urls import url

from recipes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
     # ex: /recipes/5/
    url(r'^recept/(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^recept/nytt/', views.new, name='new'),
]