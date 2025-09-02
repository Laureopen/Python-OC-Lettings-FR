from django.shortcuts import render

# Vue d'accueil générale - reste dans l'app principale
def index(request):
    return render(request, 'oc_lettings_site/index.html')