# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20171022_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='identity',
            field=models.IntegerField(verbose_name='\u8eab\u4efd', choices=[(0, '\u4e3b\u59d4'), (1, '\u526f\u4e3b\u59d4'), (2, '\u4f1a\u5458')]),
        ),
    ]
