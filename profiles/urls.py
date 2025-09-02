from django.urls import path
from . import views

app_name = 'profiles'  # Espace de noms

urlpatterns = [
    path('', views.index, name='index'),  # Était profiles_index
    path('<str:username>/', views.profile, name='profile'),
]