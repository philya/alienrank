from django.shortcuts import render

from rank.models import Domain

def home(request):
    
    domains = Domain.objects.all().order_by('-post_count', '-score_average')
    return render(request, 'base.html', {'domains': domains})
