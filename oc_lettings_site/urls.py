from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Page d'accueil générale
    path('lettings/', include('lettings.urls')),  # Espace de noms lettings
    path('profiles/', include('profiles.urls')),  # Espace de noms profiles
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # En dev uniquement : servir les statiques même si DEBUG=False
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)