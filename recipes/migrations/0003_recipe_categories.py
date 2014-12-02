# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=multiselectfield.db.fields.MultiSelectField(default=1, max_length=9, choices=[(1, b'Svenskt'), (2, b'Asiatiskt'), (3, b'Mexikanskt'), (4, b'Spanskt'), (5, b'Indiskt')]),
            preserve_default=True,
        ),
    ]
