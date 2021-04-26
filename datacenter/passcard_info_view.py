import datetime

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    # Программируем здесь
    person_visits= Visit.objects.filter(passcard=passcard)
    this_passcard_visits = [{
            "entered_at": visit.entered_at,
            "duration": format_duration(get_duration(visit)),
            "is_strange": visit.is_visit_long()
        } for visit in person_visits]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, "passcard_info.html", context)


def get_duration(visit):
    if visit.leaved_at:
        time_in_vault = (visit.leaved_at - visit.entered_at).total_seconds()
    else:
        time_in_vault = (timezone.localtime() - visit.entered_at).total_seconds()
    return time_in_vault


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int((duration % 3600) % 60)
    time_in_vault = datetime.time(hour=hours, minute=minutes, second=seconds)
    return time_in_vault
