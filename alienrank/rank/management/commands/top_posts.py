
# Standard
import csv
import datetime

# Django
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# AR
from rank.models import Domain, MediaProperty, Post

PARAM_DATE_FORMAT = '%Y%m%d%H%M'

class Command(BaseCommand):
    args = ''
    help = 'Export Top Posts'

    def handle(self, *args, **options):

        top_place = 25
        begin_str = args[0]
        end_str = args[1]

        begin = datetime.datetime.strptime(begin_str, PARAM_DATE_FORMAT)
        end = datetime.datetime.strptime(end_str, PARAM_DATE_FORMAT)

        print begin, end
        result = Post.objects.filter(created__gte=begin, created__lt=end, top_place__lte=top_place).order_by('top_place', '-created')

        outfile = open(args[2], 'wb')
        writer = csv.writer(outfile)
        writer.writerow([
            "ID",
            "Title",
            "Created",
            "Top Place",
            "URL",
            "Score",
            "Permalink",
            "Domain",
            "Domain Type",
            "Site",
        ])

        for post in result:
            row = [
                post.id,
                post.title,
                post.created,
                post.top_place,
                post.link.url,
                post.score,
                post.permalink,
                post.domain.name,
                post.domain.domain_type,
            ]
            if post.domain.media_property:
                row.append(
                    post.domain.media_property.name)
            else:
                row.append(None)

            utf8_row = []
            for i in row:
                if isinstance(i, unicode):
                    utf8_row.append(i.encode('utf8'))
                else:
                    utf8_row.append(i)
                
            writer.writerow(utf8_row)

        outfile.close()



                
        
