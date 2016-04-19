# Django related imports
from django.db import transaction
from django.contrib.auth.models import User

# Rest framework related imports
from rest_framework import serializers
from rest_framework import filters

# Local app related imports
from .models import Issues, increment_issue_number

class USER_MODELSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, style={'input_type': 'password'})

    class Meta:
        model = User

        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'username', 'is_staff', 'is_active')

class IssuesSerializer(serializers.ModelSerializer):
    issue_owner = USER_MODELSerializer(required=False)
    assigned_to_user = USER_MODELSerializer(required=False)
    filter_backends = (filters.SearchFilter,)
    class Meta:
        model = Issues
        fields = ('id', 'issue_no','issue_owner', 'title', 'assigned_to_user', 'owner_phone_number','description', 'status', 'issue_priority', 'classification', 'snapshot', 'due_date','created')


