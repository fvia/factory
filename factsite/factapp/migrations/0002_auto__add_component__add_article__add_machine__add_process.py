# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Component'
        db.create_table('factapp_component', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['factapp.Article'])),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('factapp', ['Component'])

        # Adding model 'Article'
        db.create_table('factapp_article', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('process', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['factapp.Process'])),
        ))
        db.send_create_signal('factapp', ['Article'])

        # Adding model 'Machine'
        db.create_table('factapp_machine', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('process', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['factapp.Process'])),
        ))
        db.send_create_signal('factapp', ['Machine'])

        # Adding model 'Process'
        db.create_table('factapp_process', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('factapp', ['Process'])


    def backwards(self, orm):
        # Deleting model 'Component'
        db.delete_table('factapp_component')

        # Deleting model 'Article'
        db.delete_table('factapp_article')

        # Deleting model 'Machine'
        db.delete_table('factapp_machine')

        # Deleting model 'Process'
        db.delete_table('factapp_process')


    models = {
        'factapp.article': {
            'Meta': {'object_name': 'Article'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Process']"})
        },
        'factapp.component': {
            'Meta': {'object_name': 'Component'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.FloatField', [], {})
        },
        'factapp.machine': {
            'Meta': {'object_name': 'Machine'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Process']"})
        },
        'factapp.process': {
            'Meta': {'object_name': 'Process'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['factapp']