
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
    r = praw.Reddit(settings.BOT_USER_AGENT)
    r.config.store_json_result = True
    
    res = r.get_hot(limit=100)

    s = Snapshot.create(res)

    Domain.update_counts_all()
    MediaProperty.update_counts_all()
        
