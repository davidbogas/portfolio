import os
from django.conf import settings


address_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/address-black-icon.svg')

with open(address_svg_path, 'r') as svg_file:
    address = svg_file.read()

email_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/email-black-icon.svg')

with open(email_svg_path, 'r') as svg_file:
    email = svg_file.read()

github_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/github-black-icon.svg')

with open(github_svg_path, 'r') as svg_file:
    github = svg_file.read()

linkedin_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/linkedin-black-icon.svg')

with open(linkedin_svg_path, 'r') as svg_file:
    linkedin = svg_file.read()

twitter_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/x-black-icon.svg')

with open(twitter_svg_path, 'r') as svg_file:
    twitter = svg_file.read()

instagram_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/instagram-black-icon.svg')

with open(instagram_svg_path, 'r') as svg_file:
    instagram = svg_file.read()

youtube_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/youtube-black-icon.svg')

with open(youtube_svg_path, 'r') as svg_file:
    youtube = svg_file.read()

dribbble_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/dribbble-black-icon.svg')

with open(dribbble_svg_path, 'r') as svg_file:
    dribbble = svg_file.read()

behance_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/behance-black-icon.svg')

with open(behance_svg_path, 'r') as svg_file:
    behance = svg_file.read()

twitch_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/twitch-black-icon.svg')

with open(twitch_svg_path, 'r') as svg_file:
    twitch = svg_file.read()

cv_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/cv-black-icon.svg')

with open(cv_svg_path, 'r') as svg_file:
    cv = svg_file.read()

link_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/link-black-icon.svg')

with open(link_svg_path, 'r') as svg_file:
    link = svg_file.read()

building_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/building-black-icon.svg')

with open(building_svg_path, 'r') as svg_file:
    building = svg_file.read()