
from .models import UserData, Theme
from .icons import address, email, github, linkedin, twitter, instagram, youtube, dribbble, behance, twitch, link, building, cv


def context(request):
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

    return {
        'user_data': user_data,
        'theme': theme,
        'theme_object': theme_object,
        'address_icon': address,
        'email_icon': email,
        'github_icon': github,
        'linkedin_icon': linkedin,
        'twitter_icon': twitter,
        'instagram_icon': instagram,
        'youtube_icon': youtube,
        'dribbble_icon': dribbble,
        'behance_icon': behance,
        'twitch_icon': twitch,
        'cv_icon': cv,
        'link_icon': link,
        'building_icon': building,
    }