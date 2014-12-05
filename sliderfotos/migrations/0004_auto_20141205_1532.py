# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sliderfotos', '0003_auto_20141205_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foto',
            old_name='titulo_slider',
            new_name='nombre_de_imagen',
        ),
    ]
