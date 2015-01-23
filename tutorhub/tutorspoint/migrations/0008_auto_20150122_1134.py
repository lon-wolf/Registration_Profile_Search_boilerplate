# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0007_auto_20150121_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_profile',
            name='hfee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='lfee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
