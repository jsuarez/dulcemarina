# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_producto', models.CharField(max_length=100)),
                ('descripcion_producto', models.CharField(max_length=800)),
                ('imagen_producto', models.ImageField(upload_to=b'')),
                ('pub_date', models.DateTimeField(verbose_name=b'fecha publicada')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
