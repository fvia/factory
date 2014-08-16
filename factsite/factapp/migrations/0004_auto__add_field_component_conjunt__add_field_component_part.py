# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Component.conjunt'
        db.add_column('factapp_component', 'conjunt',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['factapp.Article'], related_name='conjunt', default='X'),
                      keep_default=False)

        # Adding field 'Component.part'
        db.add_column('factapp_component', 'part',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['factapp.Article'], related_name='part', default='X'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Component.conjunt'
        db.delete_column('factapp_component', 'conjunt_id')

        # Deleting field 'Component.part'
        db.delete_column('factapp_component', 'part_id')


    models = {
        'factapp.article': {
            'Meta': {'object_name': 'Article'},
            'code': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Process']"})
        },
        'factapp.component': {
            'Meta': {'object_name': 'Component'},
            'conjunt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Article']", 'related_name': "'conjunt'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Article']", 'related_name': "'part'"}),
            'quantity': ('django.db.models.fields.FloatField', [], {})
        },
        'factapp.machine': {
            'Meta': {'object_name': 'Machine'},
            'code': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Process']"})
        },
        'factapp.process': {
            'Meta': {'object_name': 'Process'},
            'code': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['factapp']