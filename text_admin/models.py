from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from redactor.fields import RedactorField


class CachedManager(models.Manager):

    def get_from_cache(self, key):
        """
        Fetches the snippet from cache.

        Returns a `Snippet` object or `None`.

        This method adds every queried key to the cache to ensure that misses
        doesn't continue to generate database lookups. Since `None` is the
        default return value for a cache miss, the method uses -1 as the miss
        value. If this is returned we know that the value should not be present
        in the database, either.
        """
        snippet = cache.get('snippet:{0}'.format(key))

        if snippet == -1:
            return None

        if snippet is None:
            try:
                snippet = Snippet.objects.get(key=key)
            except Snippet.DoesNotExist:
                cache.set('snippet:{0}'.format(key), -1)
            else:
                cache.set('snippet:{0}'.format(key), snippet)

        return snippet

class RedactorCachedManager(models.Manager):

    def get_from_cache(self, key):
        """
        Fetches the snippet from cache.

        Returns a `Snippet` object or `None`.

        This method adds every queried key to the cache to ensure that misses
        doesn't continue to generate database lookups. Since `None` is the
        default return value for a cache miss, the method uses -1 as the miss
        value. If this is returned we know that the value should not be present
        in the database, either.
        """
        snippet = cache.get('rsnippet:{0}'.format(key))

        if snippet == -1:
            return None

        if snippet is None:
            try:
                snippet = RedactorSnippet.objects.get(key=key)
            except RedactorSnippet.DoesNotExist:
                cache.set('rsnippet:{0}'.format(key), -1)
            else:
                cache.set('rsnippet:{0}'.format(key), snippet)

        return snippet



class Snippet(models.Model):
    """
    Model for storing snippets of text for replacement in templates.
    """
    key = models.CharField(max_length=100, primary_key=True)
    text = models.TextField()
    objects = CachedManager()

    class Meta:
        ordering = ('key',)

    def __unicode__(self):
        return self.key


class RedactorSnippet(models.Model):
    """
    Model for storing snippets of text for replacement in templates.
    """
    key = models.CharField(max_length=100, primary_key=True)
    text = RedactorField()
    objects = RedactorCachedManager()

    class Meta:
        ordering = ('key',)

    def __unicode__(self):
        return self.key


@receiver(post_save, sender=Snippet)
def cache_snippet(sender, **kwargs):
    """Update the cached copy of the snippet on creation or change"""
    instance = kwargs.pop('instance')
    cache.set('snippet:{0}'.format(instance.key), instance)


@receiver(post_delete, sender=Snippet)
def clear_snippet(sender, **kwargs):
    """Remove the cached copy of the snippet after deletion"""
    instance = kwargs.pop('instance')
    cache.delete('snippet:{0}'.format(instance.key))


@receiver(post_save, sender=RedactorSnippet)
def cache_rsnippet(sender, **kwargs):
    """Update the cached copy of the snippet on creation or change"""
    instance = kwargs.pop('instance')
    cache.set('rsnippet:{0}'.format(instance.key), instance)


@receiver(post_delete, sender=RedactorSnippet)
def clear_rsnippet(sender, **kwargs):
    """Remove the cached copy of the snippet after deletion"""
    instance = kwargs.pop('instance')
    cache.delete('rsnippet:{0}'.format(instance.key))
