# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0018_remove_servicio_descripcion_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='descripcion_servicio',
            field=ckeditor.fields.RichTextField(default=datetime.date(2014, 12, 15), help_text='Redacta una descripcion del servicio'),
            preserve_default=False,
        ),
    ]
