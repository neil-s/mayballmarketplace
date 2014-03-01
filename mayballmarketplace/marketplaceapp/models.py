from django.db import models
from datetime import date

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    # cover_image = models.ImageField()

    @property
    def is_not_in_past(self):
        return self.start_date >= date.today()

    def __str__(self):
        return self.name

class TicketClass(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.name
