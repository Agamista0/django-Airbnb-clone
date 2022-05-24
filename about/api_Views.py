from rest_framework import generics
from rest_framework.permissions import IsAdminUser 
from .serializers import FQASerializer ,aboutSerializer
from .models import FAQ ,About
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes


class faq_api_view(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FQASerializer
    permission_classes = [IsAdminUser]

# class about_api_view(generics.ListAPIView):
#     queryset = About.objects.all()
#     serializer_class = aboutSerializer
#     # permission_classes = [IsAdminUser] 

@api_view(['GET'])
def about_api_view (reqeust):
    queryset = About.objects.all()
    data = aboutSerializer(queryset ,many=True).data
    return Response({"success" :True , "data " : data})