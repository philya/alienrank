# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0004_auto_20150120_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshot',
            name='listing',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='snapshot',
            name='listing_limit',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
