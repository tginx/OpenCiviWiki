# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_representative_official_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representative',
            name='account',
        ),

    ]
