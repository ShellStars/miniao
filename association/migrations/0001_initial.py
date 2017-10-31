# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assocarticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('associntro', models.TextField(default='', verbose_name='\u5b66\u4f1a\u7b80\u4ecb')),
                ('pic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u4f1a\u5fbd')),
                ('constitution', models.TextField(default='', verbose_name='\u7ae0\u7a0b')),
                ('picintro', models.TextField(default='', verbose_name='\u4f1a\u5fbd\u7b80\u4ecb')),
            ],
            options={
                'verbose_name': '\u5b66\u4f1a\u7b80\u4ecb',
                'verbose_name_plural': '\u5b66\u4f1a\u7b80\u4ecb',
            },
        ),
        migrations.CreateModel(
            name='Peoplearticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(verbose_name='\u7b49\u7ea7', choices=[(0, '\u4e3b\u59d4'), (1, '\u526f\u4e3b\u59d4'), (2, '\u4f1a\u5458')])),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('pic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5934\u50cf')),
                ('hospital', models.CharField(max_length=70, verbose_name='\u533b\u9662')),
                ('introduce', models.TextField(default='', verbose_name='\u7b80\u4ecb', blank=True)),
                ('specialty', models.TextField(default='', verbose_name='\u6280\u672f\u7279\u957f', blank=True)),
                ('postscript', models.TextField(default='', verbose_name='\u7f16\u540e\u8bed', blank=True)),
                ('weixinpic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801', blank=True)),
                ('weibopic', models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5fae\u535a\u4e8c\u7ef4\u7801', blank=True)),
            ],
            options={
                'verbose_name': '\u7f16\u59d4',
                'verbose_name_plural': '\u7f16\u59d4',
            },
        ),
    ]
