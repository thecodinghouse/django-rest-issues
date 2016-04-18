__author__ = 'gaurav'

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import patterns, include, url

# from django.conf.urls import url
# from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'issue', IssueViewSet)

urlpatterns = router.urls

urlpatterns = patterns('',
                       url(r'^api/rest/', include(router.urls)),
                       url(r'^api/issue-list/', issue_list, name="issue_list"),
                       url(r'^api/issue-details/(?P<issue_id>[0-9]+)', issue_details, name="issue_details"),
                       url(r'^api/update-issue-status/', update_issue_status, name="update_issue_status"),
                       url(r'^api/add-comment-data/', add_comment_data, name="add_comment_data"),
                       url(r'^api/update-assigned-to/', update_assigned_to, name="update_assigned_to")
                        )