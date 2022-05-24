from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Post_list_api (request):
    all_post = Post.objects.all()
    data=PostSerializer(all_post , many=True).data
    return Response({'Succcess':True , 'Post List':data })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Post_detail_api (request ,id):
    single_post =Post.objects.get(id=id) 
    data=PostSerializer(single_post).data
    return Response({'Succcess':True , 'Post detail':data })

