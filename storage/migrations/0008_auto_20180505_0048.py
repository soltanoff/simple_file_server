# Generated by Django 2.0.2 on 2018-05-04 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0007_auto_20180505_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filemodel',
            old_name='file_name',
            new_name='title',
        ),
    ]
