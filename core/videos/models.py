from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    numSubscrible = models.IntegerField()

    class Meta:
        db_table = 'video_users'

class Videos(models.Model):
    videoid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    videourl = models.TextField()
    title = models.TextField()
    description = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    size = models.FloatField()
    numsLikes = models.FloatField()
    numsDisLikes = models.FloatField()
    numViews = models.FloatField()

    class Meta:
        db_table = 'video_details'

class Comments(models.Model):
    commentid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    videoid = models.IntegerField()
    content = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'video_comments'