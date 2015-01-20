# Standard
import datetime

#Django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# Vendor
import praw

# AR
from rank.models import Snapshot, Domain, MediaProperty

class Command(BaseCommand):
    args = ''
    help = 'Read the Reddit Homepage Top 1000'

    def handle(self, *args, **options):

        start_time = datetime.datetime.now()

        r = praw.Reddit(settings.BOT_USER_AGENT)
        r.config.store_json_result = True
        
        res = r.get_front_page(limit=1000)

        s = Snapshot.create(res)

        Domain.update_counts_all()
        MediaProperty.update_counts_all()
        
        end_time = datetime.datetime.now()

        print "Elapsed time: " + str(end_time - start_time)
        
