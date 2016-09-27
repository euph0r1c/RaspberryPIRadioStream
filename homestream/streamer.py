#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
import signal
import time
from urllib import urlopen
import json

from homestream.models import Stream, Track


class Streamer(object):
    def __init__(self, url=None):
        self.__url = url
        self.__proc = None

    def play(self):
        if self.__url is not None:
            self.__proc = subprocess.Popen(['omxplayer',  '-o', 'local', '{0}'.format(self.__url)],
                                           close_fds=True, preexec_fn=os.setsid)
        else:
            raise Exception("cannot stream from URL {0}".format(self.__url))

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, a_url):
        self.__url = a_url

    @property
    def pid(self):
        if self.__proc is not None:
            return self.__proc.pid
        else:
            return None

    @staticmethod
    def kill_process(pid):
        pid = int(pid)
        os.killpg(pid, signal.SIGKILL)
        time.sleep(1)

    @staticmethod
    def process_exists(pid):
        try:
            pid = int(pid)
            os.killpg(pid, 0)
        except OSError:
            return False
        else:
            return True


class VkStreamer(Streamer):
    __vk_token = YOUR_TOKEN
    __vk_user_id = YOUR_ID
    __vk_url = "https://api.vkontakte.ru/method/audio.get.json?uid={0}&access_token={1}".format(__vk_user_id,
                                                                                                __vk_token)
    __vk_stream = Stream.objects.get(name='VKontakte')

    def __init__(self, url=None):
        super(VkStreamer, self).__init__(url)

    def truncate_playlist(self):
        self.__vk_stream.track_set.all().delete()

    def load_playlist(self):
        response = urlopen(self.__vk_url)
        data = json.loads(response.read())

        track_list = list()

        for audio in data['response'][:50]:
            url = audio['url']
            artist = audio['artist']
            title = audio['title']
            track_list.append(Track(stream=self.__vk_stream, artist=artist, title=title, url=url))

        Track.objects.bulk_create(track_list)

    def reload_playlist(self):
        self.truncate_playlist()
        self.load_playlist()
