# Standard
import datetime

# Django
from django.http import JsonResponse

# AR
from rank.models import Post

PARAM_DATE_FORMAT = '%Y%m%d%H%M'

def post_list(request):

    result = Post.objects.all()

    media_property = request.GET.get('media_property', None)
    if media_property:
        result = result.filter(domain__media_property__name=media_property)

    top_place = int(request.GET.get('top_place', 25))
    if top_place:
        result = result.filter(top_place__lte=top_place)

    begin_str = request.GET.get('begin', None)
    if begin_str:
        begin = datetime.datetime.strptime(begin_str, PARAM_DATE_FORMAT)
        result = result.filter(created__gte=begin)

    return JsonResponse({'result': [p.api_serialize() for p in result]})

    




