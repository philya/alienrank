# Standard

# Django
from django.db import models

# Vendor
from jsonfield import JSONField

# AlienRank

class Domain(models.Model):
    name = models.CharField(max_length=200, db_index=True)

class Link(models.Model):
    url = models.URLField(max_length=2083)

class Subreddit(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    url = models.URLField()
    info_url = models.URLField()

class Redditor(models.Model):

    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20, db_index=True)
    url = models.URLField()
    info_url = models.URLField()

    comment_karma = models.IntegerField()
    link_karma = models.IntegerField()
    is_mod = models.BooleanField()

    is_gold = models.BooleanField()

    created = models.DateTimeField()

class Post(models.Model):

    id = models.CharField(max_length=10, primary_key=True)

    domain = models.ForeignKey(Domain)
    linke = models.ForeignKey(Link)

    author = models.ForeignKey(Redditor)

    score = models.IntegerField()
    ups = models.IntegerField()
    downs = models.IntegerField()
    num_comments = models.IntegerField()

    permalink = models.URLField(max_length=500)

    title = models.CharField(max_length=300)

    created = models.DateTimeField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Snapshot(models.Model):
    post = models.ForeignKey(Post)
    data = JSONField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)

