# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import core_aap.mixins
import tinymce.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('issue_no', models.CharField(max_length=500, null=True, blank=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=25, null=True, blank=True)),
                ('description', tinymce.models.HTMLField(null=True, blank=True)),
                ('status', models.CharField(default=b'Open', max_length=255, choices=[(b'Open', b'Open'), (b'On-hold', b'On-hold'), (b'Escalated', b'Escalated'), (b'Closed', b'Closed')])),
                ('issue_priority', models.CharField(default=b'None', max_length=255, choices=[(b'None', b'None'), (b'High', b'High'), (b'Medium', b'Medium'), (b'Low', b'Low')])),
                ('classification', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Question', b'Question'), (b'Promblem', b'Promblem'), (b'Feauture', b'Feauture'), (b'Suggestions', b'Suggestions'), (b'Improvemnt', b'Improvemnt'), (b'Other', b'Other')])),
                ('owner_role', models.CharField(blank=True, max_length=255, null=True, choices=[(b'EMPLOYEE', b'Employee'), (b'CONSULTANT', b'Consultant'), (b'OWNER', b'Owner'), (b'WRONG', b'Wrong')])),
                ('snapshot', models.FileField(max_length=500, upload_to=core_aap.mixins.get_attachment_file_path, null=True, verbose_name=b'snapshot', blank=True)),
                ('due_date', models.DateTimeField(null=True, blank=True)),
                ('assigned_to', models.ForeignKey(blank=True, to='issues.Assigned', null=True)),
                ('issue_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
    ]
