# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='image',
            field=models.ImageField(default=b'default.jpg', upload_to=b'/img/'),
        ),
    ]
