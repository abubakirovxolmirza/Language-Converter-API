from django.contrib import admin
from .models import LanguageModels, LanguageFileModels
# Register your models here.


admin.site.register(LanguageFileModels)
admin.site.register(LanguageModels)
