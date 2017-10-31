# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0002_auto_20171023_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcearticle',
            name='column',
            field=models.CharField(default='xiazai', verbose_name='\u4e0b\u8f7d', max_length=10, editable=False),
        ),
    ]
