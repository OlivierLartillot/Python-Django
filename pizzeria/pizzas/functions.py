def check_pizza_owner(request, pizza, http):
    '''Arrête l'éxécution si l'utilisateur est différent de celui qui tente d'accéder à la donnée'''
    if pizza.owner != request.user:
        raise http