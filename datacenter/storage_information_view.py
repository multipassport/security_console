from datacenter.models import Passcard, Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = [{
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": visit.format_duration(),
            "is_strange": visit.is_visit_long()
            } for visit in visits]

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, "storage_information.html", context)
