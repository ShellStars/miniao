# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_auto_20171022_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='identity',
            field=models.IntegerField(verbose_name='\u8eab\u4efd', choices=[(0, '\u533b\u751f'), (1, '\u62a4\u58eb'), (2, '\u5b66\u751f'), (3, '\u5176\u5b83')]),
        ),
    ]
