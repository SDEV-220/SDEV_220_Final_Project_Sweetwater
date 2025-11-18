from django.conf import settings
from django.db import models
from django.utils import timezone

class Log(models.Model):
    """A music tracker log."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    song = models.CharField(default="General practice", help_text="Name of song practiced.")
    instrument = models.CharField(help_text="Name of instrument practiced.")
    practice_time = models.DurationField(default="00:00:00", help_text="Time practiced, in hours-minutes-seconds.")
    practice_date = models.DateField(default=timezone.now, help_text="Date practiced.")

    def __str__(self):
        return f"{self.song} on {self.instrument} for {self.practice_time}"