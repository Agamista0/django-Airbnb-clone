from rest_framework import generics
from .models import Property
from .serializers import propertySerialzers
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

class propertyListApi(generics.ListCreateAPIView):
    serializer_class = propertySerialzers
    queryset = Property.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','description']
    permission_classes = [IsAuthenticated]

    
    
class propertyDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = propertySerialzers
    queryset = Property.objects.all()
    permission_classes = [IsAuthenticated]
