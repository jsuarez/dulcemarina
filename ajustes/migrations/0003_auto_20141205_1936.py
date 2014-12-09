# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajustes', '0002_auto_20141205_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitio',
            name='descripcion_sitio',
            field=models.TextField(max_length=156),
        ),
        migrations.AlterField(
            model_name='sitio',
            name='titulo_sitio',
            field=models.CharField(max_length=65),
        ),
    ]
