__author__ = 'gaurav'

# Django imports ------------------------------
from django.utils import timezone
from django.conf import settings

# Third party app imports ---------------------

from post_office import mail

def send_mail_data(context):
    from_email = settings.FROM_EMAIL
    to_email = context['email_to']
    date = timezone.now().date()
    if context['type'] == "Issue_Assigned":
        if len(to_email)>1:
            mail.send(
            context['email_to'],
            from_email,
            template=context['template'],
            context=context,
        )
        else:
            mail.send(
                [to_email],
                from_email,
                template=context['template'],
                context=context,
            )
    elif context['type'] == "Issue_Comment":
        mail.send(
                [to_email],
                from_email,
                template=context['template'],
                context=context,
            )
    else:
        mail.send(
            [to_email],
            from_email,
            template='IssueAssigned',
            context=context,
        )
    return "Success"