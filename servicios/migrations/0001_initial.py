# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen_original', models.ImageField(upload_to=b'media/servicios')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_servicio', models.CharField(max_length=100)),
                ('imagen_original_servicio', models.ImageField(upload_to=b'servicios')),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Servicios',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagen',
            name='servicio',
            field=models.ForeignKey(to='servicios.Servicio'),
            preserve_default=True,
        ),
    ]
