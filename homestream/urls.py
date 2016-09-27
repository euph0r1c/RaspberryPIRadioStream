from django.conf.urls import patterns, url
from homestream import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^stream(?P<stream_id>\d+)/$', views.stream, name='stream'),
                       url(r'^stream(?P<stream_id>\d+)/reload_playlist/$', views.reload_playlist,
                           name='reload_playlist'),
                       url(r'^stream(?P<stream_id>\d+)/channel(?P<channel_id>\d+)/play$', views.player, name='player'),
                       url(r'^stream(?P<stream_id>\d+)/track(?P<track_id>\d+)/play$', views.vk_player,
                           name='vk_player'))
