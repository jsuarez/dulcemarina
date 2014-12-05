# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20141205_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_original_producto',
            field=models.ImageField(upload_to=b'media/productos'),
        ),
    ]
