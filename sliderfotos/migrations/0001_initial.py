# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_de_imagen', models.CharField(max_length=50)),
                ('imagen_original_slider', models.ImageField(upload_to=b'slider')),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Slider de Fotos',
            },
            bases=(models.Model,),
        ),
    ]
