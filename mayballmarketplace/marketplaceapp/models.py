from datetime import date

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    # cover_image = models.ImageField()

    @property
    def is_not_in_past(self):
        return self.start_date >= date.today()

    @property
    def slug(self):
        return slugify(str(self))

    def __str__(self):
        return '{} {}'.format(self.name, self.start_date.year)

    def get_absolute_url(self):
        #return "test"
        return reverse('event-with-slug', kwargs={'event_id': self.id, 'slug': self.slug})


class TicketClass(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '{} - {}'.format(self.name, self.event.name)


class Offer(models.Model):
    BUY = "B"
    SELL = "S"

    OFFER_TYPES = (
        (BUY, "Buy"),
        (SELL, "Sell")
    )

    ticket_class = models.ForeignKey(TicketClass)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    made_by = models.ForeignKey(User)
    type = models.CharField(choices=OFFER_TYPES, blank=False, default=BUY, max_length=1)
    number_of_tickets = models.IntegerField()

    def __str__(self):
        return '{} : {}'.format(self.get_type_display(), self.ticket_class)

    @property
    def action(self):
        """
        Returns a string representing the opposite of offer type. If its a buy offer, the action is to sell.
        """
        if self.type == self.BUY:
            return "sell"
        else:
            return "buy"