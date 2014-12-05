# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0004_auto_20141205_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quienessomos',
            name='imagen_original_nosotros',
            field=models.ImageField(upload_to=b'nosotros'),
        ),
    ]
