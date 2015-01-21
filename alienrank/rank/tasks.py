
# Standard Library
from __future__ import absolute_import
import logging

# Django
from django.conf import settings

# Vendor
from celery import shared_task
import praw

# AR
from .models import Snapshot, Domain, MediaProperty

logger = logging.getLogger(__name__)

@shared_task
def read_reddit_top():
    #print "Reading front_page..."
    r = praw.Reddit(settings.BOT_USER_AGENT)
    r.config.store_json_result = True
    
    LIMIT = 1000

    res = r.get_front_page(limit=LIMIT)

    s = Snapshot.create(res, 'front_page', LIMIT)

    #print "Snapshot %s created with %d posts." % (s.listing, s.postsnapshot_set.all().count())

    Domain.update_counts_all()
    MediaProperty.update_counts_all()
        
