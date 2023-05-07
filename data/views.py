from django.shortcuts import render
from rest_framework import generics
from .serializers import DataSerializer
from django.http import JsonResponse
from .models import Data
# Create your views here.

class UserDataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        data = {"users": response.data}
        return JsonResponse(data, safe=False)