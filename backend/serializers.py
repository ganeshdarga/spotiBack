from rest_framework import serializers
from .models import albumsData
from .models import songsData

class albumsDataSearilizer(serializers.ModelSerializer):
    class Meta:
        model = albumsData
        fields = '__all__'

class songsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = songsData
        fields = '__all__'
