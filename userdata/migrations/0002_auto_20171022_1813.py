# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.IntegerField(max_length=2, verbose_name='\u6027\u522b'),
        ),
    ]
