# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0002_auto_20150119_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='post_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='score_average',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='score_total',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
