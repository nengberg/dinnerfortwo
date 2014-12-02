# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='title',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
    ]
