# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0010_remove_servicio_descripcion_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='descripcion_servicio',
            field=ckeditor.fields.RichTextField(default=b'', help_text='Redacta una descripcion del servicio', blank=True),
            preserve_default=True,
        ),
    ]
