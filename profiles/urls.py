"""
Configuration des routes (URLconf) pour l'application 'profiles'.

Ce module mappe les URL de l'application vers les vues correspondantes :
    - index : affiche la liste des profils
    - profile : affiche le détail d'un profil utilisateur spécifique
"""

from django.urls import path
from . import views

#: Nom d'espace (namespace) pour éviter les conflits d'URL entre applications.
app_name = 'profiles'  # Espace de noms

#: Liste des routes de l'application.
urlpatterns = [
    path('', views.index, name='index'),  # Page listant tous les profils

# Page détaillée pour un profil donné (identifié par username)
    path('<str:username>/', views.profile, name='profile'),
]
