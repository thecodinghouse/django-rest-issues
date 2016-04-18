# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_auto_20160225_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='classification',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Query', b'Query'), (b'Issue', b'Issue'), (b'Feature', b'Feature'), (b'Suggestion', b'Suggestion'), (b'Improvement', b'Improvement'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
    ]
