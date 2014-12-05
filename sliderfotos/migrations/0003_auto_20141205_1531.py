# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sliderfotos', '0002_auto_20141205_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foto',
            options={'verbose_name_plural': 'Slider de Fotos'},
        ),
        migrations.RemoveField(
            model_name='foto',
            name='imagen_slider',
        ),
        migrations.AddField(
            model_name='foto',
            name='imagen_original_slider',
            field=models.ImageField(default=datetime.date(2014, 12, 5), upload_to=b'media/slider'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foto',
            name='titulo_slider',
            field=models.CharField(default=datetime.date(2014, 12, 5), max_length=50),
            preserve_default=False,
        ),
    ]
