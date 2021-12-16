from django.shortcuts import render, get_object_or_404

# Create your views here.
from videos.models import Users, Videos, Comments, VCs
from videos.models import raw_sql_query
from videos.serializers import UsersSerializer, VideosSerializer, CommentsSerializer, VCsSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

import redis
from django.conf import settings

# connect to redis
rd = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated,)
    
class VideosViewSet(viewsets.ModelViewSet):
    
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    permission_classes = (IsAuthenticated,)
    # /api/videos/pk/vdetail/
    @action(detail=True, methods=['get'])
    def vdetail(self, request, pk=None):
        vs = get_object_or_404(Videos, videoid=pk)
        if rd.zscore("videoviews", str(vs.videoid)) == None:
            rd.zadd("videoviews", {str(vs.videoid) : vs.numViews+1.0})
        else:
            rd.zincrby("videoviews", amount=1.0, value=str(vs.videoid))

        serializer_class = VideosSerializer(vs)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    
    # /api/videos/vrank/
    @action(detail=False, methods=['get'])
    def vrank(self, request):
        #top3 rank of videos views
        rdvr = rd.zrevrange("videoviews", start=0, end=2, withscores=True, score_cast_func=float)
        vr = Videos.objects.filter(videoid__in = [i[0] for i in rdvr]).order_by("-numViews")
        serializer_class = VideosSerializer(vr, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    
    #scheduleworker - sync the views of videos from redis to postgresql
    def sync_vrank(self):
        rdvr = rd.zrevrange("videoviews", start=0, end=-1, withscores=True, score_cast_func=float)
        if rdvr is not None:
            try:
                for i in rdvr:
                    data = Videos.objects.get(videoid=i[0].decode())
                    data.numViews = i[1]
                    data.save()                    

            except:
                pass

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

    