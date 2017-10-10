# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctorarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('midpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5c01\u9762\u56fe')),
                ('name', models.CharField(max_length=256, verbose_name='\u59d3\u540d')),
                ('bigpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u6807\u9898\u56fe')),
                ('smallpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5934\u50cf')),
                ('saying', models.CharField(max_length=256, verbose_name='\u8b66\u8a00')),
                ('introduce', models.TextField(verbose_name='\u7b80\u4ecb')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9', blank=True)),
                ('selfimage', DjangoUeditor.models.UEditorField(default='', verbose_name='\u56fe\u7247', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u5927\u5bb6\u98ce\u8303',
                'verbose_name_plural': '\u5927\u5bb6\u98ce\u8303',
            },
        ),
        migrations.CreateModel(
            name='Interviewarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('source', models.CharField(max_length=256, verbose_name='\u6765\u6e90')),
                ('author', models.CharField(max_length=256, verbose_name='\u4f5c\u8005')),
                ('browser', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u91cf')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u4e13\u8bbf',
                'verbose_name_plural': '\u4e13\u8bbf',
            },
        ),
        migrations.CreateModel(
            name='Interviewclass',
            fields=[
                ('name', models.CharField(max_length=256, serialize=False, verbose_name='\u680f\u76ee\u540d\u79f0', primary_key=True, db_index=True)),
                ('slug', models.CharField(max_length=256, verbose_name='\u680f\u76ee\u7f51\u5740')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u4e13\u5bb6\u98ce\u91c7\u680f\u76ee',
                'verbose_name_plural': '\u4e13\u5bb6\u98ce\u91c7\u680f\u76ee',
            },
        ),
        migrations.AddField(
            model_name='interviewarticle',
            name='column',
            field=models.ForeignKey(verbose_name='\u5f52\u5c5e\u680f\u76ee', to='expert.Interviewclass'),
        ),
    ]
