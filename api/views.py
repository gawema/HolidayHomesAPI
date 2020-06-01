from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User

from .models import *
from .serializers import *

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        if self.request.method == 'PATCH' or self.request.method == 'DELETE':
            user = self.request.user
            return User.objects.filter(pk=user.pk)
        return User.objects.all()

class HouseList(generics.ListCreateAPIView):
    serializer_class = HouseSerializer
    queryset = House.objects.all()

class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HouseSerializer
    def get_queryset(self):
        if self.request.method == 'PATCH' or self.request.method == 'DELETE':
            user = self.request.user
            return House.objects.filter(owner=user.pk)  
        return House.objects.all()

class OwnHouseList(generics.ListAPIView):
    serializer_class = HouseSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return House.objects.filter(owner=user)

class OwnProfile(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return User.objects.filter(pk=user.pk)

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class FacilityList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

class HouseFacilityList(generics.ListCreateAPIView):
    queryset = HouseFacility.objects.all()
    serializer_class = HouseFacilitySerializer

class HouseFacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HouseFacility.objects.all()
    serializer_class = HouseFacilitySerializer

class GalleryList(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    