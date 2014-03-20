from django.shortcuts import *
from marketplaceapp.models import *


def index(request):
    return render(request, 'index.html')


def event_offers(request, event_id="1", slug=""):
    event = get_object_or_404(Event, id=event_id)
    offers = Offer.objects.filter(ticket_class__event=event)
    buy_offers = offers.filter(type='B')
    sell_offers = offers.filter(type='S')
    return render(request, 'event.html', {"buy_offers": buy_offers, "sell_offers": sell_offers})


def event_list(request):
    events = get_list_or_404(Event, start_date__gte=date.today())  # start_date >= date.today()
    return render(request, 'event_list.html', {'events': events})