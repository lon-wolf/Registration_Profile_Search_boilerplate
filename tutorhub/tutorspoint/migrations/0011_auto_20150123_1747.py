# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0010_teacher_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_profile',
            name='classes',
            field=models.CharField(max_length=100, verbose_name=b'Preferred Classes', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='mode',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='qual',
            field=models.CharField(max_length=100, verbose_name=b'Qualification', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='skills',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
