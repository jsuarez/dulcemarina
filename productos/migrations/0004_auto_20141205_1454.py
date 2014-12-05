# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20141119_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': 'Productos'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen_producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_original_producto',
            field=models.ImageField(default=datetime.date(2014, 12, 5), upload_to=b'static/img/productos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion_producto',
            field=ckeditor.fields.RichTextField(help_text='Redacta una descripcion del producto'),
        ),
    ]
