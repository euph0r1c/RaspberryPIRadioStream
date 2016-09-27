# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stream'
        db.create_table(u'homestream_stream', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('image_url', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'homestream', ['Stream'])

        # Adding model 'RadioChannel'
        db.create_table(u'homestream_radiochannel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stream', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homestream.Stream'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('nb_plays', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image_url', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'homestream', ['RadioChannel'])

        # Adding model 'Track'
        db.create_table(u'homestream_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stream', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['homestream.Stream'])),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=400)),
            ('nb_plays', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'homestream', ['Track'])

        # Adding model 'Player'
        db.create_table(u'homestream_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pid', self.gf('django.db.models.fields.IntegerField')()),
            ('stream_id', self.gf('django.db.models.fields.IntegerField')()),
            ('channel_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'homestream', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Stream'
        db.delete_table(u'homestream_stream')

        # Deleting model 'RadioChannel'
        db.delete_table(u'homestream_radiochannel')

        # Deleting model 'Track'
        db.delete_table(u'homestream_track')

        # Deleting model 'Player'
        db.delete_table(u'homestream_player')


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
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nb_plays': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stream': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['homestream.Stream']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'})
        }
    }

    complete_apps = ['homestream']