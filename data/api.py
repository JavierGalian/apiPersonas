from .models import Data
from .serializers import DataSerializer
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status #estado de respuesta 200,300 y 400

@api_view(['GET','POST'])
def data_api_view(request):
    
    #list users, listado de ususarios
    if request.method == 'GET':
        users = Data.objects.all()
        users_serializers = DataSerializer(users, many = True) #pasa de un objeto a json
        return Response(users_serializers.data, status=status.HTTP_200_OK) 
    
    #create users, registro de usuario
    elif request.method == 'POST':
        users_serializers = DataSerializer(data = request.data) #pasa de json a un objeto
        if users_serializers.is_valid():
            users_serializers.save()
            return Response(users_serializers.data, status= status.HTTP_201_CREATED) #si se convierte en un objeto => se guarda en users_serializers.data
        return Response(users_serializers.errors, status= status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
#funcion para ver los detalles de un objecto
def user_detail_view(request,pk=None):
    user = Data.objects.filter(id = pk).first() #consulta, queryset

    if user: #validation
        #retrieve
        if request.method == 'GET':
            users_serializers = DataSerializer(user)
            return Response(users_serializers.data, status= status.HTTP_200_OK)
        #update
        elif request.method == 'PUT':
            users_serializers = DataSerializer(user, data= request.data)
            #validation
            if users_serializers.is_valid():
                users_serializers.save()
                return Response(users_serializers.data, status= status.HTTP_200_OK)
            return Response(users_serializers.errors, status= status.HTTP_400_BAD_REQUEST)
        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente'}, status= status.HTTP_200_OK)#se responde con un diccionario 
    return Response({'message':'No se encontro ningun usuario con esos datos'}, status= status.HTTP_400_BAD_REQUEST)