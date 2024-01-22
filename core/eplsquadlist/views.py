from django.shortcuts import render
from .forms import EPLFormFilter
from .models import EPL

def BackEndProcessing(request):
    frontend_query = request.GET.getlist('EplTeams_query')
    backend_query = EPL.objects.all()
    backend_query_qs = backend_query.filter(Team__in=frontend_query)
    context = {
        
        'form': EPLFormFilter(),
        'playerlist': backend_query_qs
    }
    return render(request, 'index.html', context)

