from django.test import TestCase
from django.urls import reverse
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


class IndexViewTest(TestCase):

    def test_index_view_status_code(self):
        """
        Vérifie que la page d'accueil renvoie un code 200
        """
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        """
        Vérifie que le template correct est utilisé pour la page d'accueil
        """
        url = reverse('index')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'oc_lettings_site/index.html')


"""
Configuration des routes (URLconf) principales du projet 'oc_lettings_site'.

Ce module définit les correspondances entre les chemins d'URL et :
    - l'administration Django,
    - la page d'accueil,
    - les applications internes (lettings et profiles).
Il gère également la configuration des fichiers statiques.
"""


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
