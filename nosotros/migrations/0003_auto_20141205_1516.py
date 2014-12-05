# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0002_auto_20141205_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quienessomos',
            name='imagen_nosotros',
        ),
        migrations.AddField(
            model_name='quienessomos',
            name='imagen_original_nosotros',
            field=models.ImageField(default=datetime.date(2014, 12, 5), upload_to=b'media/nosotros'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quienessomos',
            name='descripcion_nosotros',
            field=ckeditor.fields.RichTextField(help_text='Redacta una descripcion'),
        ),
    ]
