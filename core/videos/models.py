from django.db import models

# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    numSubscrible = models.IntegerField()
    role = models.IntegerField()

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
    popular = models.IntegerField()

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

class VCs(models.Model):
    commentid = models.AutoField(primary_key=True)
    content = models.TextField()
    videoid = models.IntegerField()
    videourl = models.TextField()
    title = models.TextField()

    class Meta:
        db_table = 'video_vcs'

def raw_sql_query(**kwargs):
    videoid = kwargs.get('videoid')
    sql = ('SELECT vc.commentid, vc.content, vc.videoid, vd.videourl, vd.title '+
                             'FROM video_details vd, video_comments vc '+
                             'WHERE vc.videoid = vd.videoid')
    if videoid:
        result = VCs.objects.raw(sql + ' AND vc.videoid = %s', [videoid])
    else:
        result = VCs.objects.raw(sql)
    return result
