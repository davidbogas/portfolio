from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from PIL import Image
import os


class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    icon = models.FileField(upload_to='icons', validators=[FileExtensionValidator(allowed_extensions=['svg'])], verbose_name=_('Icon'))

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(max_length=100, verbose_name=_('Position'))
    company = models.CharField(max_length=100, verbose_name=_('Company'))
    description = models.TextField(verbose_name=_('Description'))
    start_date = models.DateField(verbose_name=_('Start date'))
    end_date = models.DateField(null=True, blank=True, verbose_name=_('End date'))

    def __str__(self):
        return self.position + ' - ' + self.company


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='project_images', blank=True, verbose_name=_('Image'))
    skills = models.ManyToManyField(Skill, blank=True, verbose_name=_('Skills'))
    link = models.URLField(null=True, blank=True, verbose_name=_('Link'))
    code = models.URLField(null=True, blank=True, verbose_name=_('Code'))
    date = models.DateField(verbose_name=_('Date'))

    def __str__(self):
        return self.title


class Education(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    center = models.CharField(max_length=100, verbose_name=_('Center'))
    date = models.DateField(verbose_name=_('Date'))
    link = models.URLField(null=True, blank=True, verbose_name=_('Link'))
    icon = models.FileField(upload_to='icons', validators=[FileExtensionValidator(allowed_extensions=['svg'])], null=True, blank=True, verbose_name=_('Icon'))

    def __str__(self):
        return self.name


class UserData(models.Model):
    # Personal data
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    open_to_work = models.BooleanField(default=True, verbose_name=_('Open to work'))
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Address'))
    email = models.EmailField(verbose_name=_('Email'))
    show_email = models.BooleanField(default=True, verbose_name=_('Show email'))
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True, verbose_name=_('Profile picture'))
    cv = models.FileField(upload_to='cv', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True, verbose_name=_('CV'))

    # Social links
    website = models.URLField(null=True, blank=True, verbose_name=_('Website'))
    github = models.URLField(null=True, blank=True, verbose_name=_('GitHub'))
    linkedin = models.URLField(null=True, blank=True, verbose_name=_('LinkedIn'))
    twitter = models.URLField(null=True, blank=True, verbose_name=_('Twitter'))
    instagram = models.URLField(null=True, blank=True, verbose_name=_('Instagram'))
    youtube = models.URLField(null=True, blank=True, verbose_name=_('YouTube'))
    dribbble = models.URLField(null=True, blank=True, verbose_name=_('Dribbble'))
    behance = models.URLField(null=True, blank=True, verbose_name=_('Behance'))
    twitch = models.URLField(null=True, blank=True, verbose_name=_('Twitch'))

    # Portfolio sections
    bio = models.TextField(verbose_name=_('Bio'))
    skills = models.ManyToManyField(Skill, blank=True, verbose_name=_('Skills'))
    experience = models.ManyToManyField(Experience, blank=True, verbose_name=_('Experience'))
    projects = models.ManyToManyField(Project, blank=True, verbose_name=_('Projects'))
    studies = models.ManyToManyField(Education, blank=True, verbose_name=_('Education'))

    active = models.BooleanField(default=True, verbose_name=_('Active'))

    def save(self, *args, **kwargs):
        if self.active:
            if self.pk is None or UserData.objects.filter(active=True).exclude(pk=self.pk).exists():
                UserData.objects.filter(active=True).exclude(pk=self.pk).update(active=False)

        super(UserData, self).save(*args, **kwargs)

        if self.profile_picture:
            img_path = self.profile_picture.path

            if os.path.exists(img_path):
                img = Image.open(img_path)

                width, height = img.size
                if width > height:
                    new_width = 400
                    new_height = int(new_width * height / width)
                else:
                    new_height = 400
                    new_width = int(new_height * width / height)

                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                img = img.convert('RGB')

                img.save(img_path, 'JPEG', quality=90)

    def __str__(self):
        return f"{self.name} - {self.title} {'[ACTIVE]' if self.active else ''}"


class Theme(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    primary = models.CharField(max_length=7, verbose_name=_('Primary color'))
    secondary = models.CharField(max_length=7, verbose_name=_('Secondary color'))
    background = models.CharField(max_length=7, verbose_name=_('Background color'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    def save(self, *args, **kwargs):
        if self.active:
            if self.pk is None or Theme.objects.filter(active=True).exclude(pk=self.pk).exists():
                Theme.objects.filter(active=True).exclude(pk=self.pk).update(active=False)

        super(Theme, self).save(*args, **kwargs)

    def __str__(self):
        return self.name