from rest_framework import serializers
from .models import Data

class DataSerializer (serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
        read_only_fields = ('created_at', )

#SERIALIZERS = SU TAREA ES TOMAR LA ESTRUCTURA DE UN MODELO Y LO CONVIERTE EN FORMATO JSON 
# --SI SE USA FIELDS ENTONCES NO SE PUEDE USAR EXCLUDE
# --SI NO DE USA FIELDS ENTONCES SE PUEDE HACER EXCLUDE