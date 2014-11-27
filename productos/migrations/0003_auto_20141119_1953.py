# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141104_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(upload_to=b'img/productos'),
        ),
    ]
