from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    house = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'house'
            ]
    

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
        
class HouseSerializer(serializers.ModelSerializer):
    # house_facility = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = House
        fields = [
            'id',
            'title',
            'description',
            'street',
            'number',
            'floor',
            'direction',
            'vacancy',
            'price_per_night',
            'longitude',
            'laditude',
            'owner'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        house = House.objects.create(
            owner=user, 
            title = validated_data['title'],
            description = validated_data['description'],
            street = validated_data['street'],
            number = validated_data['number'],
            floor = validated_data['floor'],
            direction = validated_data['direction'],
            vacancy = validated_data['vacancy'],
            price_per_night = validated_data['price_per_night'],
            longitude = validated_data['longitude'],
            laditude = validated_data['laditude']
            # **validated_data
        )
        return house


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = [ 
            'user',
            'house',
            'description',
            'date_of_reservation',
            'date_booking_from',
            'date_booking_to',
            'status',
        ]

class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = [ 
            'id'
            'name',
        ]

class HouseFacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseFacility
        fields = [ 
            'house'
            'facility',
        ]

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = [ 
            'image'
            'house',
        ]

