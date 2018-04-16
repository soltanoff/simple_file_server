# -*- coding: utf-8 -*-
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(_('Title'), max_length=255)
    datetime = models.DateTimeField(_('Publication date'), default=datetime.now)
    description = models.TextField(_('Description'), max_length=100000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class PostModel(models.Model):
    class Meta:
        ordering = ['-datetime']

    title = models.CharField(_('Title'), max_length=255)
    datetime = models.DateTimeField(_('Publication date'), default=datetime.now)
    # category = models.ForeignKey(
    #     CategoryModel,
    #     on_delete=models.CASCADE,
    #     # primary_key=True,
    # )
    entry = RichTextUploadingField(_('Entry'), max_length=2000, config_name='simple_toolbar')
    content = RichTextUploadingField(_('Content'), max_length=100000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def getUrl(self):
        return '/post/%s' % self.id

    def getAllContent(self):
        return ''.join(map(lambda x: '%s' % str(x), (self.entry, self.content)))
