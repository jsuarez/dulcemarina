# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20141205_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_original_producto',
            field=models.ImageField(upload_to=b'productos'),
        ),
    ]
