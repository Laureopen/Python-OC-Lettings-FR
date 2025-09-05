"""
Configuration des routes (URLconf) principales du projet 'oc_lettings_site'.

Ce module définit les correspondances entre les chemins d'URL et :
    - l'administration Django,
    - la page d'accueil,
    - les applications internes (lettings et profiles).
Il gère également la configuration des fichiers statiques.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

#: Liste des routes principales du projet.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Page d'accueil générale
    path('lettings/', include('lettings.urls')),  # Espace de noms lettings
    path('profiles/', include('profiles.urls')),  # Espace de noms profiles
]


# Configuration des fichiers statiques
if settings.DEBUG:
    #: En mode DEBUG : servir les fichiers statiques via Django.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # En dev uniquement : servir les statiques même si DEBUG=False
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)