# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion_producto',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='producto',
            name='pub_date',
            field=models.TimeField(auto_now=True),
        ),
    ]
