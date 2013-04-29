# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'web_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=10)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Language'])

        # Adding model 'Page'
        db.create_table(u'web_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Language'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Page'], null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Page'])

        # Adding model 'Actor'
        db.create_table(u'web_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Actor'])

        # Adding model 'Play'
        db.create_table(u'web_play', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'web', ['Play'])

        # Adding model 'PlayPhoto'
        db.create_table(u'web_playphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('play', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Play'])),
        ))
        db.send_create_signal(u'web', ['PlayPhoto'])

        # Adding model 'PlayInformation'
        db.create_table(u'web_playinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('play', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Play'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Language'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web', ['PlayInformation'])

        # Adding model 'Performance'
        db.create_table(u'web_performance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('play', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Play'])),
            ('show_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'web', ['Performance'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'web_language')

        # Deleting model 'Page'
        db.delete_table(u'web_page')

        # Deleting model 'Actor'
        db.delete_table(u'web_actor')

        # Deleting model 'Play'
        db.delete_table(u'web_play')

        # Deleting model 'PlayPhoto'
        db.delete_table(u'web_playphoto')

        # Deleting model 'PlayInformation'
        db.delete_table(u'web_playinformation')

        # Deleting model 'Performance'
        db.delete_table(u'web_performance')


    models = {
        u'web.actor': {
            'Meta': {'object_name': 'Actor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'web.language': {
            'Meta': {'ordering': "['order']", 'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '10'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'web.page': {
            'Meta': {'ordering': "['order']", 'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Language']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Page']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'web.performance': {
            'Meta': {'object_name': 'Performance'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'play': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Play']"}),
            'show_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'web.play': {
            'Meta': {'object_name': 'Play'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'web.playinformation': {
            'Meta': {'object_name': 'PlayInformation'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Language']"}),
            'play': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Play']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.playphoto': {
            'Meta': {'object_name': 'PlayPhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'play': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Play']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['web']