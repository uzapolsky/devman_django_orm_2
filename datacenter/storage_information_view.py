from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration

def storage_information_view(request):

    non_closed_visits = Visit.objects.filter(leaved_at = None)

    for visit in non_closed_visits:
      visit.duration = format_duration(visit.get_duration())

    context = {
        "non_closed_visits": non_closed_visits
    }
    
    return render(request, 'storage_information.html', context)
