from datetime import date

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    # cover_image = models.ImageField()

    @property
    def is_not_in_past(self):
        return self.start_date >= date.today()

    def __str__(self):
        return '{} {}'.format(self.name, self.start_date.year)


class TicketClass(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '{} - {}'.format(self.name, self.event.name)


class Offer(models.Model):
    OFFER_TYPE_CHOICES = (
        ("B", "Buy"),
        ("S", "Sell"),
    )

    ticket_class = models.ForeignKey(TicketClass)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    made_by = models.ForeignKey(User)
    type = models.CharField(choices=OFFER_TYPE_CHOICES, max_length=1)
    number_of_tickets = models.IntegerField()

    def __str__(self):
        return '{} : {}'.format(self.type, self.ticket_class)