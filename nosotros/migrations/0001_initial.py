# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuienesSomos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_nosotros', models.CharField(max_length=100)),
                ('descripcion_nosotros', ckeditor.fields.RichTextField(help_text='Redacta una descripcion')),
                ('imagen_original_nosotros', models.ImageField(upload_to=b'nosotros', blank=True)),
                ('pub_date', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Nosotros',
            },
            bases=(models.Model,),
        ),
    ]
