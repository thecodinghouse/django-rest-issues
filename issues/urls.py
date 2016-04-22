from __future__ import absolute_import, unicode_literals
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'issue', IssueViewSet)

urlpatterns = router.urls
