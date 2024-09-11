from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image
import os


class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.FileField(upload_to='icons', validators=[FileExtensionValidator(allowed_extensions=['svg'])])

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.position + ' - ' + self.company


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images', blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    link = models.URLField(null=True, blank=True)
    code = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    name = models.CharField(max_length=100)
    center = models.CharField(max_length=100)
    date = models.DateField()
    link = models.URLField(null=True, blank=True)
    icon = models.FileField(upload_to='icons', validators=[FileExtensionValidator(allowed_extensions=['svg'])], null=True, blank=True)

    def __str__(self):
        return self.name


class UserData(models.Model):
    # Personal data
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    open_to_work = models.BooleanField(default=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    show_email = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    cv = models.FileField(upload_to='cv', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True, blank=True)

    # Social links
    website = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    dribbble = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)
    twitch = models.URLField(null=True, blank=True)

    # Portfolio sections
    bio = models.TextField()
    skills = models.ManyToManyField(Skill, blank=True)
    experience = models.ManyToManyField(Experience, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    studies = models.ManyToManyField(Education, blank=True)

    active = models.BooleanField(default=True)

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
