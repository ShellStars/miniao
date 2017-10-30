# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0005_auto_20171022_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='certificate',
            field=models.FileField(upload_to='/uploads/images/certificate/', verbose_name='\u8bc1\u4e66', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.CharField(max_length=30, verbose_name='\u6240\u5728\u79d1\u5ba4', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hospital',
            field=models.CharField(max_length=70, verbose_name='\u6240\u5728\u533b\u9662', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='integralnum',
            field=models.IntegerField(default=0, verbose_name='\u79ef\u5206', editable=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u533b\u5e08\u804c\u79f0', blank=True),
        ),
    ]
