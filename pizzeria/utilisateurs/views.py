
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    '''inscrire un nouvel utilisateur'''
    if request.method != 'POST':
        # formulaire vide
        form = UserCreationForm()
    else:
        # Traiter le formulaire rempli
        form = UserCreationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        #ouvrir session user et rediriger vers page d'accueil
        login(request, new_user)
        return redirect('pizzas:index')

    # Formulaire vierge ou invalide
    title = "login"
    context = {'form' : form, 'title': title}
    return render(request, 'registration/register.html', context) 