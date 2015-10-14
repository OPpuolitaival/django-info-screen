# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoScreen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Added', db_index=True)),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Last time edited', null=True)),
                ('delay_in_sec', models.IntegerField(default=5, verbose_name='Delay in seconds')),
                ('title', models.CharField(default=b'', max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'ordering': ['timestamp'],
                'verbose_name': 'InfoScreen',
                'verbose_name_plural': 'InfoScreen',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Added', db_index=True)),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Last time edited', null=True)),
                ('title', models.CharField(default=b'', max_length=255, verbose_name='Title')),
                ('start', models.DateTimeField(db_index=True, null=True, verbose_name='view starting time', blank=True)),
                ('end', models.DateTimeField(db_index=True, null=True, verbose_name='view ending time', blank=True)),
                ('type', models.PositiveIntegerField(default=1, db_index=True, verbose_name='view type', choices=[(0, 'iframe'), (1, 'image')])),
                ('url', models.URLField(null=True, verbose_name='url', blank=True)),
                ('image_file', models.FileField(upload_to=b'info_view/%Y/%m/%d', null=True, verbose_name='image file', blank=True)),
            ],
            options={
                'ordering': ['start'],
                'verbose_name': 'Page',
                'verbose_name_plural': 'Page',
            },
        ),
        migrations.AddField(
            model_name='infoscreen',
            name='pages',
            field=models.ManyToManyField(to='info_screen.Page', verbose_name='InfoScreen'),
        ),
    ]
