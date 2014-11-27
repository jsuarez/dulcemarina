# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_servicio', models.CharField(max_length=100)),
                ('descripcion_servicio', models.TextField(max_length=800)),
                ('imagen_servicio', models.ImageField(upload_to=b'')),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
