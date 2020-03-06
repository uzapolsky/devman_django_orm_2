from django.db import models

from django.utils import timezone

def format_duration(duration):  
    return '{}ч {}м {}с'.format(int(duration.total_seconds()//3600), int(duration.total_seconds()%3600//60),int(duration.total_seconds()%60))
    


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


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

    def get_duration(self):
      if not self.leaved_at:
        now = timezone.now()
        delta = now-self.entered_at
      else:
        delta = self.leaved_at-self.entered_at
      return delta

    def is_visit_long(self, minutes=60):
      return self.get_duration().total_seconds()//60 > minutes

    

    
