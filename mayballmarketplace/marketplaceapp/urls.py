from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from marketplaceapp import views

urlpatterns = patterns('',
                       #url(r'^$', views.index, name='index'),
                       url(r'^event/(?P<event_id>\d+)/$', view=views.event_offers, name='Event Offers'),
                       url(r'^event/(?P<event_id>\d+)/(?P<slug>[-\w\d]+)/$', view=views.event_offers,
                           name='Event Offers'),
)

urlpatterns += staticfiles_urlpatterns()