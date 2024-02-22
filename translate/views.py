from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import LanguageModels, LanguageFileModels
from .serializers import LanguageSerializers, LanguageFileSerializers
from .converter import CyrillicToLatin, LatinToCyrillic


class LanguageConverterView(CreateAPIView):
    queryset = LanguageModels
    serializer_class = LanguageSerializers

    def post(self, request):
        if 'context' in request.data:
            context = request.data['context']
            pattern = request.data['pattern']
            result = self._convert_text(context, pattern)
            return Response({'result': result})

        else:
            return Response({'error': 'Invalid request'})

    def _convert_text(self, context, pattern):
        result = ''
        mapping = None

        if pattern == 'cyrillic':
            mapping = CyrillicToLatin
            for char in context.replace('Sh', 'Ш').replace('Sh', 'Щ').replace('Ch', 'Ч').replace('sh', 'ш').replace('sh', 'щ').replace('ch', 'ч').replace('Oʻ', "Ў"):
                if char in mapping:
                    result += mapping[char]
                else:
                    result += char
        elif pattern == 'latin':
            mapping = LatinToCyrillic
            for char in context.replace('Ш', 'Sh').replace('Щ', 'Sh').replace('Ч', 'Ch').replace('ш', 'sh').replace('щ', 'sh').replace('ч', 'ch').replace('Ў', "Oʻ").replace('ў', "oʻ"):
                if char in mapping:
                    result += mapping[char]
                else:
                    result += char
        else:
            return 'Invalid pattern'

        return result


class ConvertFile(LanguageConverterView):
    queryset = LanguageFileModels
    serializer_class = LanguageFileSerializers

    def post(self, request):
        if 'file' in request.FILES:
            file = request.FILES['file']
            pattern = request.data['pattern']
            result = self._convert_file(file, pattern)
            return Response({'result': result})
        else:
            return Response({'error': 'Invalid request'})

    def _convert_file(self, file, pattern):
        if not file.name.endswith('.txt'):
            return Response({'error': 'Invalid file format. Only .txt files allowed.'})

        content = file.read().decode('utf-8').lower()
        result = self._convert_text(content, pattern)
        return result
