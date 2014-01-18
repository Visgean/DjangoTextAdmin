from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Snippet


class SnippetAdmin(TranslationAdmin):
    list_display = ('key', 'text')


admin.site.register(Snippet, SnippetAdmin)
