# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Track.title'
        db.alter_column(u'homestream_track', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Track.title'
        db.alter_column(u'homestream_track', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'homestream.player': {
            'Meta': {'object_name': 'Player'},
            'channel_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {}),
            'stream_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'homestream.radiochannel': {
            'Meta': {'object_name': 'RadioChannel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nb_plays': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['homestream.Stream']"}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        },
        u'homestream.stream': {
            'Meta': {'object_name': 'Stream'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'homestream.track': {
            'Meta': {'object_name': 'Track'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb_plays': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['homestream.Stream']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'})
        }
    }

    complete_apps = ['homestream']