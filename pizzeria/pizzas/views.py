from django.shortcuts import render, redirect

from .models import Pizza, Topping, Pizza_Comment
from .forms import * 
from django.contrib.auth.decorators import login_required
from django.http import Http404
from pizzas.functions import check_pizza_owner

# Create your views here.
def index(request):
    toppings = Topping.objects.all()
    pizze = Pizza.objects.all()
    context = {'toppings': toppings, 'pizze': pizze}
    return render(request, 'pizzas/index.html', context)

@login_required
def pizzas(request):
    pizzas = Pizza.objects.filter(owner=request.user)
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html',context)

@login_required
def pizzas_toppings(request, pizza_id):
    '''Description des ingrédients d'une pizza'''
    pizza = Pizza.objects.get(id=pizza_id)    

    # Formulaire
    if request.method != 'POST':
        form = PizzaCommentForm()
    else:
        form = PizzaCommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.pizza = pizza
            new_comment.save()
            #rediriger vers une page commentaire
        return redirect('pizzas:index') 
    
    # Commentaires
    # récupérer les commentaires attachés à cette pizza
    comments = Pizza_Comment.objects.filter(pizza=pizza.id).order_by('-date_added')
    # il faudra tester dans la vue si > 0 pour afficher les commentaires 

    is_not_owner = False
    if pizza.owner != request.user:
        is_not_owner = True
    toppings = pizza.topping_set.all()
    context = {'form': form,
               'is_not_owner': is_not_owner, 
               'pizza': pizza, 
               'toppings': toppings,
               'comments': comments,
               }
    return render(request, 'pizzas/topping.html',context)

@login_required
def new_pizza(request):
    '''Ajouter une nouvelle pizza'''
    if request.method != 'POST':
        #Aucune donnée soumise, réation d'un formulaire vide
        form = PizzaForm()
    else:
        #Des données POST soumises ! Il faut les traiter
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()

            return redirect('pizzas:pizzas')

    context = {'form': form}
    return render(request, 'pizzas/new_pizza.html', context)

@login_required
def edit_pizza(request, pizza_id):
    '''Modfier une pizza'''
    pizza = Pizza.objects.get(id=pizza_id)
    check_pizza_owner(request, pizza, Http404)
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

@login_required
def delete_pizza(request, pizza_id):
    '''Modfier une pizza'''

    pizza = Pizza.objects.get(id=pizza_id)
    check_pizza_owner(request, pizza, Http404)
    pizza.delete()

    return redirect('pizzas:pizzas')

@login_required
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

@login_required
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

@login_required
def delete_topping(request,topping_id):
    '''Supprimer un ingrédient'''
    Topping.objects.get(id=topping_id).delete()

    return redirect('pizzas:index')

@login_required
def comment_pizza(request, pizza_id):
    '''Permet a l'utilisateur de commenter une pizza'''


    return redirect('pizzas:index')
