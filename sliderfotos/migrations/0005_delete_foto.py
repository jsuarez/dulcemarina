# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sliderfotos', '0004_auto_20141205_1532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Foto',
        ),
    ]
