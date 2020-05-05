from django.shortcuts import render
from rest_framework import generics

from .models import House
from .serializers import HouseSerializer


class ListHouse(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class DetailHouse(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
