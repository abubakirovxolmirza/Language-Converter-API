from rest_framework import serializers
from .models import LanguageModels, LanguageFileModels


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = LanguageModels
        fields = '__all__'


class LanguageFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = LanguageFileModels
        fields = '__all__'
