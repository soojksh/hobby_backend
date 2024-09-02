from rest_framework import serializers
from .models import Place



class PlaceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Place
        fields = '__all__'



    
