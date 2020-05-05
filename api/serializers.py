from rest_framework import serializers
from .models import House
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    house = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'house']

        
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'owner',
        )
        model = House