import os
from django.conf import settings


email_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/email-black-icon.svg')

with open(email_svg_path, 'r') as svg_file:
    email = svg_file.read()

github_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/github-black-icon.svg')

with open(github_svg_path, 'r') as svg_file:
    github = svg_file.read()

linkedin_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/linkedin-black-icon.svg')

with open(linkedin_svg_path, 'r') as svg_file:
    linkedin = svg_file.read()

cv_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/cv-black-icon.svg')

with open(cv_svg_path, 'r') as svg_file:
    cv = svg_file.read()

link_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/link-black-icon.svg')

with open(link_svg_path, 'r') as svg_file:
    link = svg_file.read()

building_svg_path = os.path.join(settings.STATIC_ROOT, 'icons/building-black-icon.svg')

with open(building_svg_path, 'r') as svg_file:
    building = svg_file.read()