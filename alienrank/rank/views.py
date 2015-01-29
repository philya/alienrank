# Standard
import datetime

# Django
from django.shortcuts import render
from django.http import Http404

# AR
from rank.models import Domain, MediaProperty, Snapshot, Post
from rank.forms import PostFilterForm

PARAM_DATE_FORMAT = '%Y%m%d%H%M'

def home(request):
    
    domains = Domain.objects.all().order_by('-score_total', '-post_count', '-score_average')
    mps = MediaProperty.objects.filter(top_post__isnull=False).filter(top_post__top_place__isnull=False).order_by('top_post__top_place', '-score_total')

    last_snapshot = Snapshot.objects.order_by('-added')[0]

    return render(request, 'sites.html', {
        'domains': domains,
        'mps': mps,
        'last_snapshot': last_snapshot,
    })

def post_list(request):

    fform = PostFilterForm(request.GET)

    if not fform.is_valid():
        raise Http404()

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

    if fform.cleaned_data['hide_cdn']:
        result = result.exclude(domain__domain_type='cdn')

    if fform.cleaned_data['hide_reddit']:
        result = result.exclude(domain__media_property__name='reddit.com')


    result = result.order_by('top_place', '-score')
    last_snapshot = Snapshot.objects.order_by('-added')[0]

    return render(request, 'post_list.html', {
        'posts': result,
        'last_snapshot': last_snapshot,
        'fform': fform,
    })

