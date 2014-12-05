# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajustes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitio',
            options={'verbose_name_plural': 'Ajustes Generales'},
        ),
    ]
