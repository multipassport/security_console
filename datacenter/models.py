import datetime

from django.db import models
from django.utils import timezone

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def is_visit_long(self, suspicious_visit_time_in_seconds = 3600):
        is_long = False
        if self.leaved_at:
            visit_duration = (self.leaved_at - self.entered_at).total_seconds()
            if (visit_duration > suspicious_visit_time_in_seconds):
                is_long = True
        else:
            is_long = True
        return is_long


    def get_duration(self):
        time_in_vault = (timezone.localtime() - self.entered_at).total_seconds()
        return time_in_vault


    def format_duration(self):
        hours = int(self.get_duration() // 3600)
        minutes = int((self.get_duration() % 3600) // 60)
        seconds = int((self.get_duration() % 3600) % 60)
        time_in_vault = datetime.time(hour=hours, minute=minutes, second=seconds)
        return time_in_vault


