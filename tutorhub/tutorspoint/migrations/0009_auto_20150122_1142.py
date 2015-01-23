# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0008_auto_20150122_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_profile',
            name='hfee',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='lfee',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
