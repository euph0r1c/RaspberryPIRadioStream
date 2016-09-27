from django.db import models


class Stream(models.Model):
    name = models.CharField(max_length=20)
    image_url = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class RadioChannel(models.Model):
    stream = models.ForeignKey(Stream)
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=200, default='')
    nb_plays = models.IntegerField(default=0)
    image_url = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Track(models.Model):
    stream = models.ForeignKey(Stream)
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=400, default='')
    nb_plays = models.IntegerField(default=0)

    def __unicode__(self):
        return self.artist + ' - ' + self.title

    def __str__(self):
        return self.artist + ' - ' + self.title


class Player(models.Model):
    pid = models.IntegerField()
    stream_id = models.IntegerField()
    channel_id = models.IntegerField()