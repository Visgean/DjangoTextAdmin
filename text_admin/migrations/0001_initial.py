# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Snippet'
        db.create_table(u'text_admin_snippet', (
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'text_admin', ['Snippet'])

        # Adding model 'RedactorSnippet'
        db.create_table(u'text_admin_redactorsnippet', (
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('text', self.gf('redactor.fields.RedactorField')()),
        ))
        db.send_create_signal(u'text_admin', ['RedactorSnippet'])


    def backwards(self, orm):
        # Deleting model 'Snippet'
        db.delete_table(u'text_admin_snippet')

        # Deleting model 'RedactorSnippet'
        db.delete_table(u'text_admin_redactorsnippet')


    models = {
        u'text_admin.redactorsnippet': {
            'Meta': {'ordering': "('key',)", 'object_name': 'RedactorSnippet'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'text': ('redactor.fields.RedactorField', [], {})
        },
        u'text_admin.snippet': {
            'Meta': {'ordering': "('key',)", 'object_name': 'Snippet'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['text_admin']