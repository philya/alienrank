
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# AR
from rank.models import Domain, MediaProperty

class Command(BaseCommand):
    args = ''
    help = 'Classify Domains'

    def handle(self, *args, **options):

        CHOICES = {
            "m": "main",
            "c": "cdn",
            "s": "sub",
            "r": "reddit",
        }

        for d in Domain.objects.filter(media_property__isnull=True):
            while True:
                print d.name, "(Main/Cdn/Sub/Reddit):",
                choice_char = raw_input().lower()
                if choice_char in CHOICES:
                    domain_type = CHOICES[choice_char]
                    break

            d.domain_type = domain_type

            if domain_type == "main":
                d.media_property = MediaProperty.update(d.name)

            if domain_type == "reddit":
                d.media_property = MediaProperty.update("reddit.com")

            if (domain_type == "cdn") or (domain_type == "sub"):
                d.media_property = MediaProperty.update(raw_input())

            d.save()

        Domain.update_counts_all()
        MediaProperty.update_counts_all()





        
