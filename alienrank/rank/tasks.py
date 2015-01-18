
# Standard Library
from __future__ import absolute_import
import logging

# Django

# Vendor
from celery import shared_task

# AR
from .models import Snapshot

logger = logging.getLogger(__name__)

@shared_task
def read_reddit_top():
    print "Scheduled task!"

