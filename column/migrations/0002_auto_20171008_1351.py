# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('column', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'ordering': ['name'], 'verbose_name': '\u8d44\u8baf\u680f\u76ee', 'verbose_name_plural': '\u8d44\u8baf\u680f\u76ee'},
        ),
    ]
