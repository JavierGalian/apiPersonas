from rest_framework import serializers
from .models import Data

class DataSerializer (serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'name', 'last_name', 'age', 'created_at')
        read_only_fields = ('created_at', )