from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import translator, TranslationOptions

from .models import Snippet, RedactorSnippet

class AddendumTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Snippet, AddendumTranslationOptions)
translator.register(RedactorSnippet, AddendumTranslationOptions)



class SnippetAdmin(TranslationAdmin):
    list_display = ('key', 'text')


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(RedactorSnippet, SnippetAdmin)
