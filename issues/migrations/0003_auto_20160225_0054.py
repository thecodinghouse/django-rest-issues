# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20160223_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='assigned_to',
            field=models.ForeignKey(related_name='assigned_to', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issues',
            name='issue_owner',
            field=models.ForeignKey(related_name='issue_owner', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
