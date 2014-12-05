# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0004_auto_20141205_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='imagen_servicio',
        ),
        migrations.AddField(
            model_name='imagen',
            name='imagen_original',
            field=models.ImageField(default=datetime.date(2014, 12, 5), upload_to=b'media/servicios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicio',
            name='imagen_original_servicio',
            field=models.ImageField(default=datetime.date(2014, 12, 5), upload_to=b'media/servicios'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion_servicio',
            field=ckeditor.fields.RichTextField(help_text='Redacta una descripcion del servicio'),
        ),
    ]
