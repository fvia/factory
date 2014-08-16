# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Component.n'
        db.add_column('factapp_component', 'n',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Article.weight'
        db.add_column('factapp_article', 'weight',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Component.n'
        db.delete_column('factapp_component', 'n')

        # Deleting field 'Article.weight'
        db.delete_column('factapp_article', 'weight')


    models = {
        'factapp.article': {
            'Meta': {'object_name': 'Article'},
            'code': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['factapp.Process']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        'factapp.component': {
            'Meta': {'object_name': 'Component'},
            'conjunt': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conjunt'", 'to': "orm['factapp.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n': ('django.db.models.fields.IntegerField', [], {}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'part'", 'to': "orm['factapp.Article']"}),
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