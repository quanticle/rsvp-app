from django.db import models
import django.utils.timezone

# Create your models here.
class Event(models.Model):
    event_name = models.TextField()
    event_description = models.TextField()
    event_time = models.DateTimeField(default=django.utils.timezone.now)

class Rsvp(models.Model):
    name = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
