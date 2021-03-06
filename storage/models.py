# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from storage.apps import StorageConfig


class FileModel(models.Model):
    class Meta:
        ordering = ['upload_date', 'count']
        verbose_name = _('File')

    title = models.CharField(_('Title'), max_length=20)
    notes = models.CharField(_('File notes'), max_length=20, null=True)
    upload_date = models.DateTimeField(_('Upload date'), null=True, default=datetime.now, blank=True)
    count = models.IntegerField(_('Download counter'), default=0)
    file = models.FileField(_('Source'), upload_to=StorageConfig.upload_to)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @property
    def file_name(self):
        return self.file.name[len(StorageConfig.upload_to):]

    @property
    def url(self):
        return '/%s/download_file/%s/' % (StorageConfig.name, self.pk)
