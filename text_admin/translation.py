from modeltranslation.translator import translator, TranslationOptions

from .models import Snippet, RedactorSnippet

class AddendumTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Snippet, AddendumTranslationOptions)
translator.register(RedactorSnippet, AddendumTranslationOptions)

