from django.shortcuts import render

from rank.models import Domain, MediaProperty

def home(request):
    
    domains = Domain.objects.all().order_by('-score_total', '-post_count', '-score_average')
    mps = MediaProperty.objects.filter(top_post__isnull=False).filter(top_post__top_place__isnull=False).order_by('top_post__top_place', '-score_total')

    return render(request, 'base.html', {'domains': domains, 'mps': mps})
