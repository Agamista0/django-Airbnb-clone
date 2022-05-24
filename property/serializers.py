from .models import Property
from rest_framework import serializers


class propertySerialzers(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"