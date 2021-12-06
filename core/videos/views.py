from django.shortcuts import render

# Create your views here.
from videos.models import Users, Videos, Comments, VCs
from videos.models import raw_sql_query
from videos.serializers import UsersSerializer, VideosSerializer, CommentsSerializer, VCsSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)
    
class VideosViewSet(viewsets.ModelViewSet):
    
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    permission_classes = (IsAuthenticated,)
        
class CommentsViewSet(viewsets.ModelViewSet):
    
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)
    
class VCsViewSet(viewsets.ModelViewSet):
    
    queryset = VCs.objects.all()
    serializer_class = VCsSerializer
    permission_classes = (IsAuthenticated,)
    

    
    # /api/vcs/pk/vcdetail/
    @action(detail=True, methods=['get'])
    def vcdetail(self, request, pk=None):
        vcs = raw_sql_query(videoid = pk)
        serializer_class = VCsSerializer(vcs, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    # /api/vcs/vcall/
    @action(detail=False, methods=['get'])
    def vcall(self, request):
        vcs = raw_sql_query()
        serializer_class = VCsSerializer(vcs, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

