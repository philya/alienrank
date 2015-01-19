from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# Vendor
import praw

# AR
from rank.models import Snapshot

class Command(BaseCommand):
    args = ''
    help = 'Read the Reddit top 100'

    def handle(self, *args, **options):

        r = praw.Reddit(settings.BOT_USER_AGENT)
        r.config.store_json_result = True
        
        res = r.get_top(limit=100)

        s = Snapshot.create(res)
        
