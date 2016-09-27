from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from homestream.models import Stream, Player
from homestream import streamer


def index(request):
    try:
        v_player = Player.objects.get(id=1)
    except Player.DoesNotExist:
        stream_list = Stream.objects.all().order_by('-name')
        context = {'stream_list': stream_list}

        return render(request, 'homestream/index.html', context)
    else:
        if streamer.Streamer.process_exists(v_player.pid):
            v_stream = get_object_or_404(Stream, pk=v_player.stream_id)
            v_channel = v_stream.radiochannel_set.get(pk=v_player.channel_id)
            return render(request, 'homestream/play_channel.html', {'stream': v_stream, 'pid': v_player.pid,
                                                                    'channel': v_channel})
        else:
            v_player.delete()
            return HttpResponseRedirect(reverse('homestream:index'))


def stream(request, stream_id):
    my_stream = get_object_or_404(Stream, pk=stream_id)
    try:
        v_player = Player.objects.get(id=1)
    except Player.DoesNotExist:
        if my_stream.name == 'VKontakte':
            html_page = 'music_stream.html'
        else:
            html_page = 'radio_stream.html'
        return render(request, 'homestream/'+html_page, {'stream': my_stream})
    else:
        if streamer.Streamer.process_exists(v_player.pid):
            v_stream = get_object_or_404(Stream, pk=v_player.stream_id)
            v_channel = v_stream.radiochannel_set.get(pk=v_player.channel_id)
            return render(request, 'homestream/play_channel.html', {'stream': v_stream, 'pid': v_player.pid,
                                                                    'channel': v_channel})
        else:
            v_player.delete()
            return HttpResponseRedirect(reverse('homestream:stream', args=(my_stream.id,)))


def player(request, stream_id, channel_id):
    c = get_object_or_404(Stream, pk=stream_id)
    selected_channel = c.radiochannel_set.get(pk=channel_id)
    try:
        v_player = Player.objects.get(id=1)
    except Player.DoesNotExist:
        if 'stop' in request.POST:
            return HttpResponseRedirect(reverse('homestream:stream', args=(stream_id,)))
        else:
            radiostreamer = streamer.Streamer(selected_channel.url)
            radiostreamer.play()

            selected_channel.nb_plays += 1
            selected_channel.save()

            v_player = Player(id=1, pid=radiostreamer.pid, stream_id=c.id, channel_id=selected_channel.id)
            v_player.save()

            return render(request, 'homestream/play_channel.html', {'stream': c, 'pid': radiostreamer.pid,
                                                                    'channel': selected_channel})
    else:
        if 'stop' in request.POST:
            v_player.delete()
            if streamer.Streamer.process_exists(v_player.pid):
                streamer.Streamer.kill_process(v_player.pid)
            return HttpResponseRedirect(reverse('homestream:stream', args=(stream_id,)))
        else:
            c = get_object_or_404(Stream, pk=v_player.stream_id)
            selected_channel = c.radiochannel_set.get(pk=v_player.channel_id)
            return render(request, 'homestream/play_channel.html', {'stream': c, 'pid': v_player.pid,
                                                                    'channel': selected_channel})


def vk_player(request, stream_id, track_id):
    c = get_object_or_404(Stream, pk=stream_id)
    selected_track = c.track_set.get(pk=track_id)
    try:
        v_player = Player.objects.get(id=1)
    except Player.DoesNotExist:
        if 'stop' in request.POST:
            return HttpResponseRedirect(reverse('homestream:stream', args=(stream_id,)))
        else:
            vkstreamer = streamer.VkStreamer(selected_track.url)
            vkstreamer.play()

            selected_track.nb_plays += 1
            selected_track.save()

            v_player = Player(id=1, pid=vkstreamer.pid, stream_id=c.id, channel_id=selected_track.id)
            v_player.save()

            return render(request, 'homestream/play_vk.html', {'stream': c, 'pid': vkstreamer.pid,
                                                               'track': selected_track})
    else:
        if 'stop' in request.POST:
            v_player.delete()
            if streamer.Streamer.process_exists(v_player.pid):
                streamer.Streamer.kill_process(v_player.pid)
            return HttpResponseRedirect(reverse('homestream:stream', args=(stream_id,)))
        else:
            c = get_object_or_404(Stream, pk=v_player.stream_id)
            selected_track = c.track_set.get(pk=v_player.channel_id)
            return render(request, 'homestream/play_vk.html', {'stream': c, 'pid': v_player.pid,
                                                               'track': selected_track})


def reload_playlist(request, stream_id):
    vk_streamer = streamer.VkStreamer()
    vk_streamer.reload_playlist()
    return HttpResponseRedirect(reverse('homestream:stream', args=(stream_id,)))

