# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(max_length=2083)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('score', models.IntegerField()),
                ('ups', models.IntegerField()),
                ('downs', models.IntegerField()),
                ('num_comments', models.IntegerField()),
                ('permalink', models.URLField(max_length=500)),
                ('title', models.CharField(max_length=300)),
                ('created', models.DateTimeField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Redditor',
            fields=[
                ('id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, db_index=True)),
                ('url', models.URLField()),
                ('info_url', models.URLField()),
                ('comment_karma', models.IntegerField()),
                ('link_karma', models.IntegerField()),
                ('is_mod', models.BooleanField()),
                ('is_gold', models.BooleanField()),
                ('created', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', jsonfield.fields.JSONField(null=True, blank=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='rank.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, db_index=True)),
                ('url', models.URLField()),
                ('info_url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to='rank.Redditor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='domain',
            field=models.ForeignKey(to='rank.Domain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='linke',
            field=models.ForeignKey(to='rank.Link'),
            preserve_default=True,
        ),
    ]
