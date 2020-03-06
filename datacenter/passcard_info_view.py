from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.filter(passcode = passcode)

    this_passcard_visits = Visit.objects.filter(passcard=passcard[0])

    for visit in this_passcard_visits:
      visit.duration = format_duration(visit.get_duration())

    context = {
        "passcard": passcard[0],
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
