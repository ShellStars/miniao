# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='checknum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telnum', models.IntegerField(verbose_name='\u624b\u673a\u53f7', db_index=True)),
                ('checknum', models.IntegerField(null=True, verbose_name='\u77ed\u4fe1\u9a8c\u8bc1\u7801', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('sex', models.CharField(max_length=50, verbose_name='\u6027\u522b')),
                ('telnum', models.IntegerField(verbose_name='\u624b\u673a\u53f7', db_index=True)),
                ('email', models.EmailField(max_length=254, verbose_name='\u7535\u5b50\u90ae\u7bb1')),
                ('hospital', models.CharField(max_length=256, verbose_name='\u6240\u5728\u533b\u9662')),
                ('department', models.CharField(max_length=256, verbose_name='\u6240\u5728\u79d1\u5ba4')),
                ('title', models.CharField(max_length=256, verbose_name='\u533b\u5e08\u804c\u79f0')),
                ('password', models.CharField(max_length=256, verbose_name='\u5bc6\u7801')),
                ('identity', models.CharField(max_length=256, verbose_name='\u8eab\u4efd')),
                ('certificate', models.FileField(upload_to='E:\\Node\\python\\miniao\\django\\django-minicms-a89bbbfb3478578f0746a20a193b557c74d3ca92/media/uploads/images/certificate/', max_length=256, verbose_name='\u8bc1\u4e66')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('isfgpwd', models.BooleanField(default=False, verbose_name='\u5fd8\u8bb0\u5bc6\u7801')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
