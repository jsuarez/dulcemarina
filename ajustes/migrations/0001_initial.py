# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_sitio', models.CharField(max_length=100)),
                ('descripcion_sitio', models.TextField(max_length=800)),
                ('mail_sitio', models.EmailField(max_length=75)),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
