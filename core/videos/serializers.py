from rest_framework import serializers
from videos.models import Users, Videos, Comments, VCs


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # fields = '__all__'
        fields = ('userid', 'name', 'email', 'createTime', 'numSubscrible', 'role')

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        # fields = '__all__'
        fields = ('videoid', 'userid', 'videourl', 'title', 'description', 'createTime', 'size', 'numsLikes', 'numsDisLikes', 'numViews', 'popular')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        # fields = '__all__'
        fields = ('commentid', 'userid', 'videoid', 'content', 'createTime')

class VCsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCs
        # fields = '__all__'
        fields = ('commentid', 'content', 'videoid','videourl', 'title')


