from django.urls import path
from .views import LanguageConverterView, ConvertFile

urlpatterns = [
    path('text/', LanguageConverterView.as_view(), name='convert-text'),
    path('file/', ConvertFile.as_view(), name='convert-file'),
]
