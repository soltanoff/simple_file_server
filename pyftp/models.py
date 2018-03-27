# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models


class FileModel(models.Model):
    file_name = models.CharField('Title', max_length=20)
    notes = models.CharField('File notes', max_length=20, null=True)
    upload_date = models.DateTimeField('Upload date', null=True, default=datetime.now, blank=True)
    count = models.IntegerField('Download counter', default=0)
    file = models.FileField('Source')

    def __str__(self):
        return self.file_name

    def getUrl(self):
        return '/download_file/%s' % self.id
