# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.AlterModelOptions(
            name='standardarticle',
            options={'verbose_name': '\u5176\u4ed6', 'verbose_name_plural': '\u5176\u4ed6'},
        ),
        migrations.AlterModelOptions(
            name='standardclass',
            options={'ordering': ['name'], 'verbose_name': '\u5176\u4ed6\u680f\u76ee', 'verbose_name_plural': '\u5176\u4ed6\u680f\u76ee'},
        ),
        migrations.AlterField(
            model_name='resourcearticle',
            name='browser',
            field=models.IntegerField(default=0, verbose_name='\u4e0b\u8f7d\u91cf', editable=False),
        ),
    ]
