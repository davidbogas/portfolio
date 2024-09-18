from django.shortcuts import render, redirect
from .models import UserData, Theme


def home(request):
    if request.method == 'POST':
        theme = Theme(
            name=request.POST['theme-name'],
            primary=request.POST['primary-color'],
            secondary=request.POST['secondary-color'],
            background=request.POST['background-color'],
            active=True,
            )
        theme.save()
        return redirect('home:home')

    return render(request, 'home/index.html')