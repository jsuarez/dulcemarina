# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_producto', models.CharField(max_length=100)),
                ('descripcion_producto', ckeditor.fields.RichTextField(help_text='Redacta una descripcion del producto')),
                ('imagen_original_producto', models.ImageField(upload_to=b'productos')),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
            bases=(models.Model,),
        ),
    ]
