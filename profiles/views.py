from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):  # Renommé de profiles_index
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)  # Renommé de index.html


def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)  # Plus sûr que .get()
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
