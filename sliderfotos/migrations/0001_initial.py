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
                ('imagen_slider', models.ImageField(upload_to=b'img/slider')),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
