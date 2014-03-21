from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from marketplaceapp import views

urlpatterns = patterns('',
                       url(r'^$', view=views.event_list, name='event-list'),
                       url(r'^event/(?P<event_id>\d+)/$', view=views.event_offers, name='event-without-slug'),
                       url(r'^event/(?P<event_id>\d+)/(?P<slug>[-\w\d]+)/$', view=views.event_offers,
                           name='event-with-slug'),
                       url(r'^match/(?P<offer_id>\d+)/$', view=views.match_offer, name='match-offer'),
                       url(r'^pay/(?P<offer_id>\d+)/$', view=views.pay, name='pay'),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)

urlpatterns += staticfiles_urlpatterns()