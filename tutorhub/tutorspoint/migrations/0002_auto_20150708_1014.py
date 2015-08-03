# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorspoint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='first_profile',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='age',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='classes',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='hfee',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='lfee',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='qual',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='subjects',
        ),
        migrations.RemoveField(
            model_name='first_profile',
            name='zipcode',
        ),
        migrations.RemoveField(
            model_name='second_profile',
            name='qual',
        ),
        migrations.AddField(
            model_name='first_profile',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name=b'First Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='first_profile',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name=b'Last Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='second_profile',
            name='pic',
            field=models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/'),
            preserve_default=True,
        ),
    ]
