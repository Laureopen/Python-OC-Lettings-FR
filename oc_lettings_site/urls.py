from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Page d'accueil générale
    path('lettings/', include('lettings.urls')),  # Espace de noms lettings
    path('profiles/', include('profiles.urls')),  # Espace de noms profiles
]