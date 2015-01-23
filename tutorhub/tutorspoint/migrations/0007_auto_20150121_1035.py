# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0006_teacher_profile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_profile',
            name='classes',
            field=models.CharField(max_length=50, verbose_name=b'Preferred Classes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='exp',
            field=models.CharField(max_length=30, verbose_name=b'Teaching Experience', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='location',
            field=models.CharField(max_length=100, verbose_name=b'Preferred Locations', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='mode',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher_profile',
            name='subjects',
            field=models.CharField(max_length=100, verbose_name=b'Preferred Subjects', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='address1',
            field=models.CharField(max_length=100, verbose_name=b'Address Line 1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='address2',
            field=models.CharField(max_length=100, verbose_name=b'Address Line 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='city',
            field=models.CharField(max_length=100, verbose_name=b'City', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='country',
            field=models.CharField(max_length=100, verbose_name=b'Country', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='skills',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='state',
            field=models.CharField(max_length=100, verbose_name=b'State', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='zipcode',
            field=models.CharField(max_length=6, verbose_name=b'ZIP code', blank=True),
            preserve_default=True,
        ),
    ]
