"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from marketplaceapp.models import *
from datetime import date, timedelta

class EventTests(TestCase):
    def test_event_tommorow(self):
        tomorrow = date.today() + timedelta(days=1)
        event = Event(name="Pembroke Test Event", start_date=tomorrow)
        self.assertTrue(event.is_not_in_past)

    def test_event_today(self):
        event = Event(name="Pembroke Test Event", start_date=date.today())
        self.assertTrue(event.is_not_in_past)

    def test_event_yesterday(self):
        yesterday = date.today() - timedelta(days=1)
        event = Event(name="Pembroke Test Event", start_date=yesterday)
        self.assertFalse(event.is_not_in_past)
