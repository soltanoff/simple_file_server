# Generated by Django 2.0.2 on 2018-04-17 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180417_1911'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryModel',
            new_name='TagModel',
        ),
        migrations.RenameField(
            model_name='postmodel',
            old_name='category',
            new_name='tags',
        ),
    ]
