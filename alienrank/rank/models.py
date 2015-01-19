# Standard
import hashlib
import datetime

# Django
from django.db import models
from django.db.models import Avg, Sum

# Vendor
from jsonfield import JSONField

# AlienRank

class Domain(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    added = models.DateTimeField(auto_now_add=True)

    post_count = models.IntegerField(null=True)
    score_total = models.IntegerField(null=True)
    score_average = models.IntegerField(null=True)

    @classmethod
    def update_counts_all(cls):
        for d in Domain.objects.all():
            d.update_counts()

    def update_counts(self, save=True):
        self.post_count = self.post_set.all().count() 
        self.score_total = self.post_set.aggregate(Sum('score')).values()[0]
        score_average = self.post_set.aggregate(Avg('score')).values()[0]
        if score_average:
            self.score_average = int(round(score_average))

        if save:
            self.save()

    @classmethod
    def update(cls, name):
        try:
            domain = Domain.objects.get(name=name)
        except Domain.DoesNotExist:
            domain = Domain(name=name)
            domain.save()

        
        return domain

class Link(models.Model):
    url = models.URLField(max_length=2083)
    url_hash = models.CharField(max_length=32)

    added = models.DateTimeField(auto_now_add=True)

    @classmethod
    def update(cls, url):
        h = hashlib.md5()
        h.update(url)
        url_hash = h.hexdigest()
        try:
            link = Link.objects.get(url_hash=url_hash)
        except Link.DoesNotExist:
            link = Link(
                url_hash=url_hash,
                url=url)
            link.save()
        return link



class Subreddit(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20, db_index=True)
    url = models.URLField()
    info_url = models.URLField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def update(cls, pr):
        if pr == None:
            return None
        try:
            subreddit = Subreddit.objects.get(pk=pr.id)
        except Subreddit.DoesNotExist:
            subreddit = Subreddit(id=pr.id)

        subreddit.name = pr.url
        subreddit.url = pr._url
        subreddit.info_url = pr._info_url

        subreddit.created = datetime.datetime.utcfromtimestamp(pr.created_utc)

        subreddit.save()
        return subreddit

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

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def update(cls, pr):
        if pr == None:
            return None
        try:
            redditor = Redditor.objects.get(pk=pr.id)
        except Redditor.DoesNotExist:
            redditor = Redditor(id=pr.id)

        redditor.name = pr.name
        redditor.url = pr._url
        redditor.info_url = pr._info_url

        redditor.comment_karma = pr.comment_karma
        redditor.link_karma = pr.link_karma

        redditor.is_mod = pr.is_mod
        redditor.is_gold = pr.is_gold

        redditor.created = datetime.datetime.utcfromtimestamp(pr.created_utc)

        redditor.save()
        return redditor

class Post(models.Model):

    id = models.CharField(max_length=10, primary_key=True)

    domain = models.ForeignKey(Domain)
    link = models.ForeignKey(Link)

    author = models.ForeignKey(Redditor, null=True)

    subreddit = models.ForeignKey(Subreddit, null=True)

    score = models.IntegerField()
    ups = models.IntegerField()
    downs = models.IntegerField()
    num_comments = models.IntegerField()

    permalink = models.URLField(max_length=500)

    title = models.CharField(max_length=300)

    created = models.DateTimeField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def update(cls, postsnap, pr):
        try:
            post = Post.objects.get(pk=pr.id)
        except Post.DoesNotExist:
            post = Post(id=pr.id)

        post.domain = Domain.update(pr.domain)
        post.link = Link.update(pr.url)
        post.author = Redditor.update(pr.author)
        post.subreddit = Subreddit.update(pr.subreddit)

        post.score = pr.score
        post.ups = pr.ups
        post.downs = pr.downs
        post.num_comments = pr.num_comments
        post.permadomain = pr.permalink
        post.title = pr.title
        post.created = datetime.datetime.utcfromtimestamp(pr.created_utc)

        post.save()
        return post
            

class Snapshot(models.Model):
    added = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, praw_result):
        snapshot = Snapshot()
        snapshot.save()

        place = 0
        for p in praw_result:
            place += 1
            postsnap = PostSnapshot.create(snapshot, place, p)
            print postsnap.place, postsnap.post.title

        return snapshot


class PostSnapshot(models.Model):
    post = models.ForeignKey(Post, null=True)
    place = models.IntegerField()
    snapshot = models.ForeignKey(Snapshot)
    data = JSONField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, snapshot, place, praw_result):
        postsnap = PostSnapshot(
            place=place,
            snapshot=snapshot,
            data=praw_result.json_dict)
        postsnap.save()

        post = Post.update(postsnap, praw_result)

        postsnap.post = post
        postsnap.save()

        return postsnap

    
