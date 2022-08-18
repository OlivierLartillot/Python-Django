'''définir les motifs d'url de pizzas'''
from django.urls import path

from . import views

app_name = "pizzas"
urlpatterns = [
    # Page d'accueil
    path('', views.index, name='index'),
]