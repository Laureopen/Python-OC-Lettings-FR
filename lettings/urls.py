"""
Définition des routes (URLconf) pour l'application 'lettings'.

Ce module mappe les URL de l'application vers les vues correspondantes.
"""
from django.urls import path
from . import views

app_name = 'lettings'  #: Nom d'espace (namespace) pour éviter les conflits d'URL entre applications.

#: Liste des routes de l'application
urlpatterns = [
    path('', views.index, name='index'),  # Était lettings_index
    path('<int:letting_id>/', views.letting, name='letting'),
]
