# Standard
import datetime
import logging

#Django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# Vendor
import praw

# AR
from rank.models import Snapshot, Domain, MediaProperty

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = 'Read the Reddit Homepage Top 1000'

    def handle(self, *args, **options):

        limit = 1000

        start_time = datetime.datetime.now()

        r = praw.Reddit(settings.BOT_USER_AGENT)
        r.config.store_json_result = True
        
        res = r.get_front_page(limit=limit)

        s = Snapshot.create(res, "front_page", limit)

        Domain.update_counts_all()
        MediaProperty.update_counts_all()
        
        end_time = datetime.datetime.now()

        print "Elapsed time: " + str(end_time - start_time)
        
