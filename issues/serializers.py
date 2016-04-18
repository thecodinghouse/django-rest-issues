# Django related imports
from django.db import transaction

# Rest framework related imports
from rest_auth.registration.serializers import slugify_unicode, unique_slug
from rest_framework import serializers
from rest_framework import filters

# Local app related imports
from .models import Issues, increment_issue_number
from consultants.serializers import USER_MODELSerializer



class IssuesSerializer(serializers.ModelSerializer):
    issue_owner = USER_MODELSerializer(required=False)
    assigned_to_user = USER_MODELSerializer(required=False)
    filter_backends = (filters.SearchFilter,)
    class Meta:
        model = Issues
        fields = ('id', 'issue_no','issue_owner', 'title', 'assigned_to_user', 'owner_phone_number','description', 'status', 'issue_priority', 'classification', 'snapshot', 'due_date','created')


