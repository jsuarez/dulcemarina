# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0009_auto_20141215_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='descripcion_servicio',
        ),
    ]
