# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u4e13\u9898\u6807\u9898', db_index=True)),
                ('slug', models.CharField(max_length=256, verbose_name='\u4e13\u9898\u7f51\u5740')),
                ('friendimage', models.ImageField(upload_to='uploads/images/meetspecial/')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u53cb\u5546\u63a8\u8350',
                'verbose_name_plural': '\u53cb\u5546\u63a8\u8350',
            },
        ),
        migrations.CreateModel(
            name='Resourcearticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('source', models.CharField(max_length=256, verbose_name='\u6765\u6e90')),
                ('author', models.CharField(max_length=256, verbose_name='\u4f5c\u8005')),
                ('browser', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u91cf')),
                ('filename', models.FileField(upload_to='uploads/files/download/', verbose_name='\u4e0a\u4f20\u6587\u4ef6')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u8d44\u6e90\u4e0b\u8f7d',
                'verbose_name_plural': '\u8d44\u6e90\u4e0b\u8f7d',
            },
        ),
        migrations.CreateModel(
            name='Resourcesclass',
            fields=[
                ('name', models.CharField(max_length=256, serialize=False, verbose_name='\u680f\u76ee\u540d\u79f0', primary_key=True, db_index=True)),
                ('slug', models.CharField(max_length=256, verbose_name='\u680f\u76ee\u7f51\u5740')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u8d44\u6e90\u4e0b\u8f7d\u680f\u76ee',
                'verbose_name_plural': '\u8d44\u6e90\u4e0b\u8f7d\u680f\u76ee',
            },
        ),
        migrations.CreateModel(
            name='Standardarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('source', models.CharField(max_length=256, verbose_name='\u6765\u6e90')),
                ('author', models.CharField(max_length=256, verbose_name='\u4f5c\u8005')),
                ('browser', models.IntegerField(verbose_name='\u6d4f\u89c8\u91cf')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u6307\u5357\u4e0e\u89c4\u8303',
                'verbose_name_plural': '\u6307\u5357\u4e0e\u89c4\u8303',
            },
        ),
        migrations.CreateModel(
            name='Standardclass',
            fields=[
                ('name', models.CharField(max_length=256, serialize=False, verbose_name='\u680f\u76ee\u540d\u79f0', primary_key=True, db_index=True)),
                ('slug', models.CharField(max_length=256, verbose_name='\u680f\u76ee\u7f51\u5740')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u6307\u5357\u4e0e\u89c4\u8303\u680f\u76ee',
                'verbose_name_plural': '\u6307\u5357\u4e0e\u89c4\u8303\u680f\u76ee',
            },
        ),
        migrations.AddField(
            model_name='standardarticle',
            name='column',
            field=models.ForeignKey(verbose_name='\u5f52\u5c5e\u680f\u76ee', to='other.Standardclass'),
        ),
        migrations.AddField(
            model_name='resourcearticle',
            name='column',
            field=models.ForeignKey(verbose_name='\u5f52\u5c5e\u680f\u76ee', to='other.Resourcesclass'),
        ),
    ]
