from django.db import models


# Create your models here.
class LanguageModels(models.Model):
    language_CHOICES = (
        ('latin', 'latin'),
        ('cyrillic', 'cyrillic'))
    context = models.TextField()
    pattern = models.CharField(max_length=20, choices=language_CHOICES)


class LanguageFileModels(models.Model):
    language_CHOICES = (
        ('latin', 'latin'),
        ('cyrillic', 'cyrillic'))
    file = models.FileField(upload_to='file/', blank=True)
    pattern = models.CharField(max_length=20, choices=language_CHOICES)
