from django.shortcuts import render

from rank.models import Domain, MediaProperty

def home(request):
    
    domains = Domain.objects.all().order_by('-score_total', '-post_count', '-score_average')
    mps = MediaProperty.objects.all().order_by('-score_total', '-post_count', '-score_average')

    return render(request, 'base.html', {'domains': domains, 'mps': mps})
