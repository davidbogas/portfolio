from django.contrib import admin
from .models import Skill, Experience, Project, Education, UserData

admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(UserData)