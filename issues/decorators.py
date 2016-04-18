__author__ = 'gaurav'

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.contrib.messages import *

def user_in_group_required(func=None, login_url=None):
    def decorator(a_view):
        def _wrapped_view(request, *args, **kwargs):
            try:
                user = request.user
                groups = Group.objects.all()
                if user.groups.all()[0] in groups:
                    return a_view(request, *args, **kwargs)
                else:
                    print "user not authenticated"
                    return HttpResponseRedirect('/api/error/')
            except:
                warning(request, "You do not have permission to perform this action.")

            return HttpResponseRedirect(login_url)

        return _wrapped_view

    if func:
        return decorator(func)
    return decorator