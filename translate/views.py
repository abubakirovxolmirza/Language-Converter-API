from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import LanguageModels, LanguageFileModels
from .serializers import LanguageSerializers, LanguageFileSerializers
from .converter import convert_file, convert_text


class LanguageConverterView(CreateAPIView):
    queryset = LanguageModels
    serializer_class = LanguageSerializers

    def post(self, request, *args, **kwargs):
        if 'context' in request.data:
            context = request.data['context']
            pattern = request.data['pattern']
            result = convert_text(context, pattern)
            return Response({'result': result})

        else:
            return Response({'error': 'Invalid request'})


class ConvertFile(LanguageConverterView):
    queryset = LanguageFileModels
    serializer_class = LanguageFileSerializers

    def post(self, request, *args, **kwargs):
        if 'file' in request.FILES:
            file = request.FILES['file']
            pattern = request.data['pattern']
            result = convert_file(file, pattern)
            return Response({'result': result})
        else:
            return Response({'error': 'Invalid request'})

