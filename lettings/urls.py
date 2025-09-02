from django.urls import path
from . import views

app_name = 'lettings'  # Espace de noms

urlpatterns = [
    path('', views.index, name='index'),  # Était lettings_index
    path('<int:letting_id>/', views.letting, name='letting'),
]