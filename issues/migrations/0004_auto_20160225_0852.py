# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0003_auto_20160225_0054'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assigned',
        ),
        migrations.RemoveField(
            model_name='issues',
            name='assigned_to',
        ),
        migrations.AddField(
            model_name='issues',
            name='assigned_to_user',
            field=models.ForeignKey(related_name='assigned_to_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
