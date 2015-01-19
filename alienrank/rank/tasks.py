
# Standard Library
from __future__ import absolute_import
import logging

# Django
from django.conf import settings

# Vendor
from celery import shared_task
import praw

# AR
from .models import Snapshot

logger = logging.getLogger(__name__)

@shared_task
def read_reddit_top():
    r = praw.Reddit(settings.BOT_USER_AGENT)
    r.config.store_json_result = True
    
    res = r.get_top(limit=100)

    s = Snapshot.create(res)
        
