# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0005_auto_20141205_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quienessomos',
            name='imagen_original_nosotros',
            field=models.ImageField(upload_to=b'nosotros', blank=True),
        ),
    ]
