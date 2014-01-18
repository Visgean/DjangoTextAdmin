# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Snippet'
        db.create_table('addendum_snippet', (
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_cs', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('addendum', ['Snippet'])


    def backwards(self, orm):
        # Deleting model 'Snippet'
        db.delete_table('addendum_snippet')


    models = {
        'addendum.snippet': {
            'Meta': {'ordering': "('key',)", 'object_name': 'Snippet'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_cs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['addendum']