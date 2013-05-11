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
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Language'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Page'], null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Page'])

        # Adding model 'Person'
        db.create_table(u'web_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('staff_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'web', ['Person'])

        # Adding model 'PersonInformation'
        db.create_table(u'web_personinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Language'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('about', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web', ['PersonInformation'])

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

        # Adding M2M table for field performers on 'Performance'
        db.create_table(u'web_performance_performers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performance', models.ForeignKey(orm[u'web.performance'], null=False)),
            ('person', models.ForeignKey(orm[u'web.person'], null=False))
        ))
        db.create_unique(u'web_performance_performers', ['performance_id', 'person_id'])

        # Adding M2M table for field designers on 'Performance'
        db.create_table(u'web_performance_designers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performance', models.ForeignKey(orm[u'web.performance'], null=False)),
            ('person', models.ForeignKey(orm[u'web.person'], null=False))
        ))
        db.create_unique(u'web_performance_designers', ['performance_id', 'person_id'])

        # Adding M2M table for field directors on 'Performance'
        db.create_table(u'web_performance_directors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performance', models.ForeignKey(orm[u'web.performance'], null=False)),
            ('person', models.ForeignKey(orm[u'web.person'], null=False))
        ))
        db.create_unique(u'web_performance_directors', ['performance_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'web_language')

        # Deleting model 'Page'
        db.delete_table(u'web_page')

        # Deleting model 'Person'
        db.delete_table(u'web_person')

        # Deleting model 'PersonInformation'
        db.delete_table(u'web_personinformation')

        # Deleting model 'Play'
        db.delete_table(u'web_play')

        # Deleting model 'PlayPhoto'
        db.delete_table(u'web_playphoto')

        # Deleting model 'PlayInformation'
        db.delete_table(u'web_playinformation')

        # Deleting model 'Performance'
        db.delete_table(u'web_performance')

        # Removing M2M table for field performers on 'Performance'
        db.delete_table('web_performance_performers')

        # Removing M2M table for field designers on 'Performance'
        db.delete_table('web_performance_designers')

        # Removing M2M table for field directors on 'Performance'
        db.delete_table('web_performance_directors')


    models = {
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
            'Meta': {'ordering': "['-show_time']", 'object_name': 'Performance'},
            'designers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'designers'", 'symmetrical': 'False', 'to': u"orm['web.Person']"}),
            'directors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'directors'", 'symmetrical': 'False', 'to': u"orm['web.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'performers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'performers'", 'symmetrical': 'False', 'to': u"orm['web.Person']"}),
            'play': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Play']"}),
            'show_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'web.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'staff_type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'web.personinformation': {
            'Meta': {'object_name': 'PersonInformation'},
            'about': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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