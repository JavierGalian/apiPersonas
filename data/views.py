from django.shortcuts import render
from rest_framework import generics
from .serializers import DataSerializer
from django.http import JsonResponse
from django.views import View
from .models import Data
# Create your views here.

class UserDataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        data = {"users": response.data}
        return JsonResponse(data, safe=False)
    

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

#class CreateUserView(View):
#    def post(self, request, *args, **kwargs):
#        #obtener los datos enviados desde el fronted
#        name = request.data.get('name')
#        last_name = request.data.get('last_name')
#        name_user = request.data.get('name_user')
#        email = request.data.get('email')
#        date_birth = request.data.get('date_birth')
#        password = request.data.get('password')

        #crear un nuevo objeto a partir de los datos recibidos
#        new_data = Data.objects.create(
#            name = name,
#            last_name = last_name,
#            name_user = name_user,
#            email = email,
#            date_birth = date_birth,
#            password = password,
#        )
#        return JsonResponse({'message':'Usuario creado exitosamente.'})