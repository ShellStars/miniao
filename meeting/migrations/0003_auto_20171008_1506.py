# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0002_auto_20171008_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetspecial',
            name='meetimage',
            field=models.ImageField(upload_to='uploads/images/meetspecial/'),
        ),
    ]
