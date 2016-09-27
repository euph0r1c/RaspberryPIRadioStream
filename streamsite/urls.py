from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^homestream/', include('homestream.urls', namespace='homestream')),
                       url(r'^$', include('homestream.urls', namespace='homestream')),
                       url(r'^admin/', include(admin.site.urls)),)
