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

def match_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    # If it's a buy offer, user_action = sell, and vice versa.
    user_action = offer.action
    return render(request, 'match.html', {'offer': offer, 'user_action': user_action})


def pay(request, offer_id):
    # Placeholder view
    return render(request, 'index.html')

