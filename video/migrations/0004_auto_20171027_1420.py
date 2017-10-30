# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20171027_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoarticle',
            name='difficulty',
            field=models.IntegerField(verbose_name='\u96be\u5ea6\u7b49\u7ea7', choices=[(0, '\u521d\u7ea7'), (1, '\u4e2d\u7ea7'), (2, '\u9ad8\u7ea7')]),
        ),
        migrations.AlterField(
            model_name='videoarticle',
            name='expert',
            field=models.CharField(max_length=20, verbose_name='\u4e13\u5bb6\u540d\u79f0'),
        ),
    ]
