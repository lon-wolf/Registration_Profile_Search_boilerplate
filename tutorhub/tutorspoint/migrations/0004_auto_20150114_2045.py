# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0003_base_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_profile',
            name='user_type',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
