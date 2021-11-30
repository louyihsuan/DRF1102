from django.shortcuts import render

# Create your views here.
from videos.models import Users, Videos, Comments
from videos.serializers import UsersSerializer, VideosSerializer, CommentsSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


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
    

