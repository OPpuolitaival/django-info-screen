# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info_screen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(verbose_name='link')),
                ('link_text', models.CharField(max_length=255, verbose_name='Link text')),
            ],
            options={
                'ordering': ['link_text'],
                'verbose_name': 'Back link',
                'verbose_name_plural': 'Back links',
            },
        ),
        migrations.AddField(
            model_name='infoscreen',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Users', blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='continuous',
            field=models.BooleanField(default=False, verbose_name='Continuous'),
        ),
        migrations.AddField(
            model_name='page',
            name='readonly',
            field=models.BooleanField(default=False, verbose_name='readonly'),
        ),
        migrations.AlterField(
            model_name='infoscreen',
            name='pages',
            field=models.ManyToManyField(to='info_screen.Page', verbose_name='InfoScreen', blank=True),
        ),
        migrations.AddField(
            model_name='infoscreen',
            name='back_link',
            field=models.ForeignKey(verbose_name='Back link', blank=True, to='info_screen.BackLink', null=True),
        ),
    ]
