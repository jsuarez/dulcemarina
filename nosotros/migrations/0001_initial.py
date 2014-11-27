# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuienesSomos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_nosotros', models.CharField(max_length=100)),
                ('descripcion_nosotros', models.TextField(max_length=800)),
                ('imagen_nosotros', models.ImageField(upload_to=b'img/nosotros')),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
