from .models import Data
from .serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DataApiView(APIView):
    def get(self, request):
        users = Data.objects.all()
        users_serializers = DataSerializer(users, many = True)
        return Response(users_serializers.data) 