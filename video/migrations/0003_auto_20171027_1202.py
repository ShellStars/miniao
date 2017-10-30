# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20171027_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoarticle',
            name='difficulty',
            field=models.IntegerField(default=3, blank=True, verbose_name='\u96be\u5ea6\u7b49\u7ea7', choices=[(0, '\u521d\u7ea7'), (1, '\u4e2d\u7ea7'), (2, '\u9ad8\u7ea7')]),
        ),
    ]
