import datetime

from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = [{
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': visit.is_visit_long()
            } for visit in visits]

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)


def get_duration(visit):
    time_in_vault = (timezone.localtime() - visit.entered_at).total_seconds()
    return time_in_vault


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int((duration % 3600) % 60)
    time_in_vault = datetime.time(hour=hours, minute=minutes, second=seconds)
    return time_in_vault
