# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('association', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assocarticle',
            name='weibopic',
            field=models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5fae\u535a\u4e8c\u7ef4\u7801', blank=True),
        ),
        migrations.AddField(
            model_name='assocarticle',
            name='weixinpic',
            field=models.ImageField(upload_to='uploads/images/doctor/', verbose_name='\u5fae\u4fe1\u4e8c\u7ef4\u7801', blank=True),
        ),
    ]
