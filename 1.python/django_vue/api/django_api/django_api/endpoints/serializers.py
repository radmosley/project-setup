from rest_framework import serializers
from .models import endPoint1

class EndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = endPoint1
        fields = (
            'name',
            'description',
            'created_at',
            'updated_at'
        )