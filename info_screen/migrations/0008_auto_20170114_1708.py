# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_screen', '0007_page_delay_in_sec'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='is_slideshow_page',
            field=models.BooleanField(default=False, verbose_name='Slideshow page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='delay_in_sec',
            field=models.IntegerField(default=5, verbose_name='Default delay in seconds'),
        ),
    ]
