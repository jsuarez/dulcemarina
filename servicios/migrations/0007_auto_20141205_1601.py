# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_auto_20141205_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen_original_servicio',
            field=models.ImageField(upload_to=b'servicios'),
        ),
    ]
