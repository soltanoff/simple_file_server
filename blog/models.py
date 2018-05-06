# -*- coding: utf-8 -*-
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class TagModel(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(_('Title'), max_length=255)
    datetime = models.DateTimeField(_('Publication date'), default=datetime.now)
    description = models.TextField(_('Description'), max_length=100000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


# TODO: polcracker: set `get_url` method as `url` property
class PostModel(models.Model):
    class Meta:
        ordering = ['-datetime']

    title = models.CharField(_('Title'), max_length=255)
    datetime = models.DateTimeField(_('Publication date'), default=datetime.now)
    tags = models.ManyToManyField(TagModel, verbose_name=_('Tags'), blank=True)
    entry = RichTextUploadingField(_('Entry'), max_length=2000, config_name='simple_toolbar')
    content = RichTextUploadingField(_('Content'), max_length=100000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_url(self):
        return '/post/%s' % self.pk

    def getAllContent(self):
        return ''.join(map(lambda x: '%s' % str(x), (self.entry, self.content)))
