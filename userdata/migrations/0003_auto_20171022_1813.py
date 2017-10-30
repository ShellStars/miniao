# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20171022_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.IntegerField(verbose_name='\u6027\u522b'),
        ),
    ]
