# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0008_auto_20141215_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcion_servicio',
            field=ckeditor.fields.RichTextField(help_text='Redacta una descripcion del servicio'),
        ),
    ]
