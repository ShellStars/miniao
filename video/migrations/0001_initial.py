# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videoarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u6807\u9898')),
                ('source', models.CharField(max_length=20, verbose_name='\u6765\u6e90')),
                ('author', models.CharField(max_length=20, verbose_name='\u4f5c\u8005')),
                ('browser', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u91cf', editable=False)),
                ('disease', models.CharField(max_length=20, verbose_name='\u75be\u75c5\u5206\u7c7b')),
                ('difficulty', models.IntegerField(verbose_name='\u96be\u5ea6\u7b49\u7ea7', choices=[(0, '\u521d\u7ea7'), (1, '\u4e2d\u7ea7'), (2, '\u9ad8\u7ea7')])),
                ('expert', models.CharField(max_length=20, verbose_name='\u4e13\u5bb6\u540d\u79f0')),
                ('other', models.CharField(max_length=20, verbose_name='\u5176\u4ed6')),
                ('zan', models.IntegerField(default=0, verbose_name='\u8d5e', editable=False)),
                ('smallpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5c01\u9762')),
                ('introduction', models.TextField(default='', verbose_name='\u7b80\u4ecb', blank=True)),
                ('video', models.FileField(upload_to='uploads/files/download/', verbose_name='\u89c6\u9891')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u89c6\u9891',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
        migrations.CreateModel(
            name='Videoclass',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='\u680f\u76ee\u540d\u79f0')),
                ('slug', models.CharField(max_length=30, serialize=False, verbose_name='\u680f\u76ee\u7f51\u5740', primary_key=True, db_index=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u89c6\u9891\u680f\u76ee',
                'verbose_name_plural': '\u89c6\u9891\u680f\u76ee',
            },
        ),
        migrations.AddField(
            model_name='videoarticle',
            name='column',
            field=models.ForeignKey(verbose_name='\u5f52\u5c5e\u680f\u76ee', to='video.Videoclass'),
        ),
    ]
