# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quienessomos',
            name='descripcion_nosotros',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='quienessomos',
            name='imagen_nosotros',
            field=models.ImageField(upload_to=b'static/img/nosotros'),
        ),
    ]
