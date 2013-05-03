# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.body'
        db.alter_column(u'web_page', 'body', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Page.body'
        db.alter_column(u'web_page', 'body', self.gf('django.db.models.fields.TextField')(default=None))

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
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'actors'", 'symmetrical': 'False', 'to': u"orm['web.Actor']"}),
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