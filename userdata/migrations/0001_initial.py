# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checknum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telnum', models.CharField(max_length=15, verbose_name='\u624b\u673a\u53f7', db_index=True)),
                ('checknum', models.CharField(max_length=10, null=True, verbose_name='\u77ed\u4fe1\u9a8c\u8bc1\u7801', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.IntegerField(verbose_name='\u7528\u6237id')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898\u540d\u79f0')),
                ('url', models.URLField(max_length=100, verbose_name='\u94fe\u63a5\u5730\u5740')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='\u6536\u85cf\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.IntegerField(verbose_name='\u7528\u6237id')),
                ('url', models.URLField(verbose_name='\u94fe\u63a5\u5730\u5740')),
                ('scorenum', models.CharField(max_length=3, verbose_name='\u6253\u5206')),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('sex', models.CharField(max_length=10, verbose_name='\u6027\u522b')),
                ('telnum', models.CharField(max_length=15, verbose_name='\u624b\u673a\u53f7', db_index=True)),
                ('email', models.EmailField(max_length=254, verbose_name='\u7535\u5b50\u90ae\u7bb1')),
                ('hospital', models.CharField(max_length=70, verbose_name='\u6240\u5728\u533b\u9662')),
                ('department', models.CharField(max_length=30, verbose_name='\u6240\u5728\u79d1\u5ba4')),
                ('title', models.CharField(max_length=30, verbose_name='\u533b\u5e08\u804c\u79f0')),
                ('password', models.CharField(verbose_name='\u5bc6\u7801', max_length=30, editable=False)),
                ('identity', models.CharField(max_length=30, verbose_name='\u8eab\u4efd')),
                ('certificate', models.FileField(upload_to='/uploads/images/certificate/', verbose_name='\u8bc1\u4e66')),
                ('integralnum', models.IntegerField(default=0, verbose_name='\u79ef\u5206')),
                ('ispass', models.BooleanField(default=False, verbose_name='\u5ba1\u6838\u901a\u8fc7')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('isfgpwd', models.BooleanField(default=False, verbose_name='\u5fd8\u8bb0\u5bc6\u7801', editable=False)),
            ],
            options={
                'ordering': ['username'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
