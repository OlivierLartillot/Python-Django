from django.shortcuts import render, redirect

from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

# Create your views here.
def index(request):
    toppings = Topping.objects.all()
    context = {'toppings': toppings}
    return render(request, 'pizzas/index.html', context)

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html',context)

def pizzas_toppings(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza' : pizza, 'toppings': toppings}
    return render(request, 'pizzas/topping.html',context)

def new_pizza(request):
    '''Ajouter une nouvelle pizza'''
    if request.method != 'POST':
        #Aucune donnée soumise, réation d'un formulaire vide
        form = PizzaForm()
    else:
        #Des données POST soumises ! Il faut les traiter
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizzas')

    context = {'form': form}
    return render(request, 'pizzas/new_pizza.html', context)

def edit_pizza(request, pizza_id):
    '''Modfier une pizza'''
    pizza = Pizza.objects.get(id=pizza_id)
    
    if request.method != 'POST':
        #Aucune donnée soumise, réation d'un formulaire vide
        form = PizzaForm(instance=pizza)
    else:
        #Des données POST soumises ! Il faut les traiter
        form = PizzaForm(instance=pizza,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizzas')

    context = {'pizza': pizza, 'form': form}
    return render(request, 'pizzas/edit_pizza.html', context)

def delete_pizza(request, pizza_id):
    '''Modfier une pizza'''
    Pizza.objects.get(id=pizza_id).delete()

    return redirect('pizzas:pizzas')

def new_topping(request):
    '''Ajouter un nouveau topping'''

    if request.method != 'POST':
        #Aucune donnée soumise, réation d'un formulaire vide
        form = ToppingForm()
    else:
        #Des données POST soumises ! Il faut les traiter
        form = ToppingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:index')

    context = {'form':form}
    return render(request, 'pizzas/new_topping.html', context)

def edit_topping(request, topping_id):
    '''Modifie un topping'''
    topping= Topping.objects.get(id=topping_id)

    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('pizzas:index')

    context = {'topping': topping, 'form': form, }
    return render(request,'pizzas/edit_topping.html', context)

def delete_topping(request,topping_id):
    '''Supprimer un ingrédient'''
    Topping.objects.get(id=topping_id).delete()

    return redirect('pizzas:index')
