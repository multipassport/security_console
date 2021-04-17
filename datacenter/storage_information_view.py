from datacenter.models import Passcard, Visit
from django.shortcuts import render


def storage_information_view(request):
    people_in_vault = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = [{
            'who_entered': person.passcard.owner_name,
            'entered_at': person.entered_at,
            'duration': format_duration(get_duration(person))
            } for person in people_in_vault]
    
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

def get_duration(visit):
    return 0

def format_duration(duration):
    return '1ч 1мин'
