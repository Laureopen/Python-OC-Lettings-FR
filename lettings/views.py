from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):  # Renommé de lettings_index
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)  # Renommé de index.html


def letting(request, letting_id):
    letting = get_object_or_404(Letting, id=letting_id)  # Plus sûr que .get()
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)