from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Prefetch
from django.forms.models import BaseInlineFormSet
from django.contrib.auth.models import Group, Permission

from django import forms

from functools import partial

# Register your models here.

from employee.models import Employee
from .models import Issues


class IssuesAdmin(admin.ModelAdmin):
    model = Issues
    list_display = ('issue_no', 'title', 'owner_phone_number', 'status', 'issue_priority', 'classification')
    # inlines = [ IssueCommentsAdmin ]

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['assigned_to_user'].queryset = User.objects.filter(groups__name='Tickets')
        return super(IssuesAdmin, self).render_change_form(request, context, args, kwargs)



admin.site.register(Issues, IssuesAdmin)
# admin.site.register(IssueComments, IssueCommentsAdmin)