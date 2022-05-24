from rest_framework import serializers 
from .models import  FAQ , About

class FQASerializer (serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'



class aboutSerializer (serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
