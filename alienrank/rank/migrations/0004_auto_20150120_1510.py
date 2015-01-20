# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0003_auto_20150119_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('post_count', models.IntegerField(null=True)),
                ('score_total', models.IntegerField(null=True)),
                ('score_average', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='domain',
            name='domain_type',
            field=models.CharField(db_index=True, max_length=10, null=True, choices=[(b'main', b'Main'), (b'cdn', b'CDN'), (b'sub', b'Subdomain'), (b'reddit', b'Reddit')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='media_property',
            field=models.ForeignKey(to='rank.MediaProperty', null=True),
            preserve_default=True,
        ),
    ]
