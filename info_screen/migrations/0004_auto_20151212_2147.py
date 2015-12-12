# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_screen', '0003_auto_20151212_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'start'], 'verbose_name': 'Page', 'verbose_name_plural': 'Page'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order', db_index=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='type',
            field=models.PositiveIntegerField(default=1, db_index=True, verbose_name='view type', choices=[(0, 'url'), (1, 'image')]),
        ),
    ]
