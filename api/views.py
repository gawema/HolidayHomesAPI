from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User

from .models import House
from .serializers import HouseSerializer
from .serializers import UserSerializer



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListHouse(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class DetailHouse(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = House.objects.all()
    serializer_class = HouseSerializer
