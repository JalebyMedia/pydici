# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0012_clientbill_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientbill',
            name='lang',
            field=models.CharField(default=b'fr-fr', max_length=10, verbose_name='Language', choices=[(b'fr-fr', 'French'), (b'en-en', 'English')]),
        ),
    ]
