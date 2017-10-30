# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name='\u6807\u9898')),
                ('source', models.CharField(max_length=20, verbose_name='\u6765\u6e90')),
                ('author', models.CharField(max_length=20, verbose_name='\u4f5c\u8005')),
                ('browser', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u91cf', editable=False)),
                ('keyword', models.CharField(max_length=30, verbose_name='\u5173\u952e\u8bcd', blank=True)),
                ('tag', models.CharField(max_length=30, verbose_name='\u6807\u7b7e', blank=True)),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='\u5185\u5bb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u836f\u68b0\u63a8\u8350',
                'verbose_name_plural': '\u836f\u68b0\u63a8\u8350',
            },
        ),
        migrations.CreateModel(
            name='Recommendclass',
            fields=[
                ('name', models.CharField(max_length=20, verbose_name='\u680f\u76ee\u540d\u79f0')),
                ('slug', models.CharField(max_length=30, serialize=False, verbose_name='\u680f\u76ee\u7f51\u5740', primary_key=True, db_index=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u836f\u68b0\u63a8\u8350\u680f\u76ee',
                'verbose_name_plural': '\u836f\u68b0\u63a8\u8350\u680f\u76ee',
            },
        ),
        migrations.AddField(
            model_name='recommendarticle',
            name='column',
            field=models.ForeignKey(verbose_name='\u5f52\u5c5e\u680f\u76ee', to='recommend.Recommendclass'),
        ),
    ]
