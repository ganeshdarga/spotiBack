from django.shortcuts import render
from rest_framework import viewsets
from .models import albumsData
from .models import songsData

from .serializers import albumsDataSearilizer
from .serializers import songsDataSerializer

class albumsDataViewSet(viewsets.ModelViewSet):
    queryset = albumsData.objects.all()
    serializer_class = albumsDataSearilizer

class songsDataViewSet(viewsets.ModelViewSet):
    queryset = songsData.objects.all()
    serializer_class = songsDataSerializer