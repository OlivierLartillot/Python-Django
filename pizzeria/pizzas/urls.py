'''définir les motifs d'url de pizzas'''
from django.urls import path

from . import views

app_name = "pizzas"
urlpatterns = [
    # Page d'accueil
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>', views.pizzas_toppings, name='pizzas_toppings'),
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    path('edit_pizza/<int:pizza_id>', views.edit_pizza, name='edit_pizza'),
    path('delete_pizza/<int:pizza_id>', views.delete_pizza, name='delete_pizza'),
    path('new_topping/', views.new_topping, name='new_topping'),
    path('edit_topping/<int:topping_id>', views.edit_topping, name='edit_topping'),
    path('delete_topping/<int:topping_id>', views.delete_topping, name='delete_topping'),

]