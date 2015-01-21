from django.shortcuts import render

from rank.models import Domain, MediaProperty, Snapshot

def home(request):
    
    domains = Domain.objects.all().order_by('-score_total', '-post_count', '-score_average')
    mps = MediaProperty.objects.filter(top_post__isnull=False).filter(top_post__top_place__isnull=False).order_by('top_post__top_place', '-score_total')

    last_snapshot = Snapshot.objects.order_by('-added')[0]

    return render(request, 'base.html', {
        'domains': domains,
        'mps': mps,
        'last_snapshot': last_snapshot,
    })
