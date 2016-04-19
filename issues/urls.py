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
