# Generated by Django 3.2.9 on 2021-12-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('videoid', models.IntegerField()),
                ('content', models.TextField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'video_comments',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('numSubscrible', models.IntegerField()),
                ('role', models.IntegerField()),
            ],
            options={
                'db_table': 'video_users',
            },
        ),
        migrations.CreateModel(
            name='VCs',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('videoid', models.IntegerField()),
                ('videourl', models.TextField()),
                ('title', models.TextField()),
            ],
            options={
                'db_table': 'video_vcs',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('videoid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('videourl', models.TextField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('size', models.FloatField()),
                ('numsLikes', models.FloatField()),
                ('numsDisLikes', models.FloatField()),
                ('numViews', models.FloatField()),
                ('popular', models.IntegerField()),
            ],
            options={
                'db_table': 'video_details',
            },
        ),
    ]
