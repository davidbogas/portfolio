from django.shortcuts import render
from .models import UserData
from .icons import email, github, linkedin, link, building, cv


def home(request):
    user = UserData.objects.get(active=True)

    # theme = "<style>:root{--primary-color:#33bbcc;--secondary-color:#ddaa00}</style>"

    context = {
        'user': user,
        'email_icon': email,
        'github_icon': github,
        'linkedin_icon': linkedin,
        'cv_icon': cv,
        'link_icon': link,
        'building_icon': building,
        # 'theme': theme,
    }

    return render(request, 'home/index.html', context)