# Generated by Django 5.1.1 on 2024-09-11 18:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('center', models.CharField(max_length=100, verbose_name='Center')),
                ('date', models.DateField(verbose_name='Date')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('icon', models.FileField(blank=True, null=True, upload_to='icons', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])], verbose_name='Icon')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('description', models.TextField(verbose_name='Description')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('icon', models.FileField(upload_to='icons', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])], verbose_name='Icon')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('primary', models.CharField(max_length=7, verbose_name='Primary color')),
                ('secondary', models.CharField(max_length=7, verbose_name='Secondary color')),
                ('background', models.CharField(max_length=7, verbose_name='Background color')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='project_images', verbose_name='Image')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('code', models.URLField(blank=True, null=True, verbose_name='Code')),
                ('skills', models.ManyToManyField(blank=True, to='home.skill', verbose_name='Skills')),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('open_to_work', models.BooleanField(default=True, verbose_name='Open to work')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('show_email', models.BooleanField(default=True, verbose_name='Show email')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics', verbose_name='Profile picture')),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='CV')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('github', models.URLField(blank=True, null=True, verbose_name='GitHub')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='LinkedIn')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='YouTube')),
                ('dribbble', models.URLField(blank=True, null=True, verbose_name='Dribbble')),
                ('behance', models.URLField(blank=True, null=True, verbose_name='Behance')),
                ('twitch', models.URLField(blank=True, null=True, verbose_name='Twitch')),
                ('bio', models.TextField(verbose_name='Bio')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('experience', models.ManyToManyField(blank=True, to='home.experience', verbose_name='Experience')),
                ('projects', models.ManyToManyField(blank=True, to='home.project', verbose_name='Projects')),
                ('skills', models.ManyToManyField(blank=True, to='home.skill', verbose_name='Skills')),
                ('studies', models.ManyToManyField(blank=True, to='home.education', verbose_name='Education')),
            ],
        ),
    ]
