# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0003_auto_20141205_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quienessomos',
            options={'verbose_name_plural': 'Nosotros'},
        ),
    ]
