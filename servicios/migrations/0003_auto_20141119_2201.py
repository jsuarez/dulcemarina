# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to=b'img/servicios'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='servicio',
            field=models.ForeignKey(to='servicios.Servicio'),
        ),
    ]
