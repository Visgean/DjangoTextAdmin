# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RedactorSnippet.text_cs'
        db.add_column(u'text_admin_redactorsnippet', 'text_cs',
                      self.gf('redactor.fields.RedactorField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RedactorSnippet.text_en'
        db.add_column(u'text_admin_redactorsnippet', 'text_en',
                      self.gf('redactor.fields.RedactorField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Snippet.text_cs'
        db.add_column(u'text_admin_snippet', 'text_cs',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Snippet.text_en'
        db.add_column(u'text_admin_snippet', 'text_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RedactorSnippet.text_cs'
        db.delete_column(u'text_admin_redactorsnippet', 'text_cs')

        # Deleting field 'RedactorSnippet.text_en'
        db.delete_column(u'text_admin_redactorsnippet', 'text_en')

        # Deleting field 'Snippet.text_cs'
        db.delete_column(u'text_admin_snippet', 'text_cs')

        # Deleting field 'Snippet.text_en'
        db.delete_column(u'text_admin_snippet', 'text_en')


    models = {
        u'text_admin.redactorsnippet': {
            'Meta': {'ordering': "('key',)", 'object_name': 'RedactorSnippet'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'text': ('redactor.fields.RedactorField', [], {}),
            'text_cs': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'})
        },
        u'text_admin.snippet': {
            'Meta': {'ordering': "('key',)", 'object_name': 'Snippet'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_cs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['text_admin']