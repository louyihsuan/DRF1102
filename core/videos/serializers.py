from rest_framework import serializers
from videos.models import Users, Videos, Comments


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # fields = '__all__'
        fields = ('userid', 'name', 'email', 'createTime', 'numSubscrible')

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        # fields = '__all__'
        fields = ('videoid', 'userid', 'videourl', 'title', 'description', 'createTime', 'size', 'numsLikes', 'numsDisLikes', 'numViews')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        # fields = '__all__'
        fields = ('commentid', 'userid', 'videoid', 'content', 'createTime')

