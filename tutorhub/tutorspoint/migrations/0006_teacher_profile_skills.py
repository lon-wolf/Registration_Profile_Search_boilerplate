# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0005_auto_20150121_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_profile',
            name='skills',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
