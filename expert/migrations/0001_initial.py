# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articletag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('maininfo', models.TextField(default='', verbose_name='\u5185\u5bb9')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('content', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('published', models.BooleanField(default=False, verbose_name='\u5ba1\u6838\u901a\u8fc7')),
            ],
            options={
                'verbose_name': '\u5ba1\u6838',
                'verbose_name_plural': '\u5ba1\u6838',
            },
        ),
        migrations.CreateModel(
            name='Doctorarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column', models.CharField(default='fengfan', verbose_name='\u5927\u5bb6\u98ce\u8303', max_length=10, editable=False)),
                ('midpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5c01\u9762\u56fe')),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('bigpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u4e3b\u56fe')),
                ('smallpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5609\u5bbe\u5934\u50cf')),
                ('saying', models.CharField(max_length=70, verbose_name='\u6458\u8981')),
                ('introduce', models.TextField(verbose_name='\u6587\u5b57\u4ecb\u7ecd')),
                ('postscript', models.TextField(verbose_name='\u7f16\u540e\u8bed')),
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
            name='Expertarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column', models.CharField(default='zhuanjia', verbose_name='\u4e13\u5bb6', max_length=10, editable=False)),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('ranks', models.CharField(max_length=10, verbose_name='\u804c\u79f0')),
                ('province', models.CharField(max_length=10, verbose_name='\u7701\u4efd')),
                ('city', models.CharField(max_length=20, verbose_name='\u57ce\u5e02')),
                ('zan', models.IntegerField(default=0, verbose_name='\u8d5e', editable=False)),
                ('hospital', models.CharField(max_length=50, verbose_name='\u533b\u9662')),
                ('department', models.CharField(max_length=30, verbose_name='\u6240\u5728\u79d1\u5ba4')),
                ('midpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5c01\u9762\u56fe')),
                ('smallpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u4e13\u5bb6\u5934\u50cf')),
                ('introduce', models.TextField(verbose_name='\u6587\u5b57\u4ecb\u7ecd')),
                ('specialty', models.TextField(verbose_name='\u6280\u672f\u7279\u957f')),
                ('postscript', models.TextField(verbose_name='\u7f16\u540e\u8bed')),
                ('weixinpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801', blank=True)),
                ('weibopic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5fae\u535a\u4e8c\u7ef4\u7801', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('published', models.BooleanField(default=True, verbose_name='\u6b63\u5f0f\u53d1\u5e03')),
            ],
            options={
                'verbose_name': '\u4e13\u5bb6',
                'verbose_name_plural': '\u4e13\u5bb6',
            },
        ),
        migrations.CreateModel(
            name='Interviewarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column', models.CharField(default='zhuanfang', verbose_name='\u4e13\u8bbf', max_length=10, editable=False)),
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
                'verbose_name': '\u4e13\u8bbf',
                'verbose_name_plural': '\u4e13\u8bbf',
            },
        ),
        migrations.CreateModel(
            name='Pictag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('pic', models.ImageField(help_text='jpgonly', upload_to='uploads/images/doctor/', verbose_name='\u56fe\u7247')),
                ('contact', models.ForeignKey(to='expert.Doctorarticle')),
            ],
        ),
        migrations.CreateModel(
            name='Videotag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898', blank=True)),
                ('video', models.FileField(help_text='mp4only', upload_to='uploads/images/doctor/', verbose_name='\u89c6\u9891', blank=True)),
                ('contact', models.ForeignKey(to='expert.Doctorarticle', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='articletag',
            name='contact',
            field=models.ForeignKey(to='expert.Doctorarticle'),
        ),
    ]
