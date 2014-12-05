# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sliderfotos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='imagen_slider',
            field=models.ImageField(upload_to=b'static/img/slider'),
        ),
    ]
