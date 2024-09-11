from django.shortcuts import render, redirect
from .models import UserData, Theme
from .icons import address, email, github, linkedin, link, building, cv


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

    if UserData.objects.filter(active=True).exists():
        user_data = UserData.objects.get(active=True)
    else:
        user_data = UserData()
        user_data.save()

    if Theme.objects.filter(active=True).exists():
        theme_object = Theme.objects.get(active=True)
        theme = f"<style>:root{{--primary-color:{theme_object.primary};--secondary-color:{theme_object.secondary};--bg-color:{theme_object.background}}}</style>"
    else:
        theme = ''
        theme_object = None

    context = {
        'user_data': user_data,
        'address_icon': address,
        'email_icon': email,
        'github_icon': github,
        'linkedin_icon': linkedin,
        'cv_icon': cv,
        'link_icon': link,
        'building_icon': building,
        'theme': theme,
        'theme_object': theme_object,
    }

    return render(request, 'home/index.html', context)