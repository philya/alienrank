# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0009_post_top_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='top_post',
            field=models.ForeignKey(related_name='+', to='rank.Post', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediaproperty',
            name='top_post',
            field=models.ForeignKey(related_name='+', to='rank.Post', null=True),
            preserve_default=True,
        ),
    ]
