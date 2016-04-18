from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel
from core_aap.mixins import BasePeople, TaggedMixin, Ownable, TimeStampedModel, Orderable, get_attachment_file_path
from django.conf import settings
from django.db import connection


# Third party apps import
from tinymce.models import HTMLField
from tenant_schemas.utils import get_tenant_model

# Local app imports ----------------

from .utils import send_mail_data

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')



# Creat unique issue number
def increment_issue_number():
    try:
        issues = Issues.objects.order_by('-pk')[0]
        if not issues:
            return '#0001'
        issue_no = issues.issue_no
        issue_int = int(issue_no.split('#')[-1])
        width = 4
        new_issue_int = issue_int + 1
        formatted = (width - len(str(new_issue_int))) * "0" + str(new_issue_int)
        new_issue_no = '#' + str(formatted)
        return new_issue_no
    except:
        new_issue_no = '#0001'
        return new_issue_no


STATUS_CHOICES = [
    ('Open', 'Open'),
    ('On-hold', 'On-hold'),
    ('Escalated', 'Escalated'),
    ('Closed', 'Closed')
]

PRIORITY_CHOICES = [
    ('None', 'None'),
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
]

CLASSIFICATION_CHOICES = [
    ('Query', 'Query'),
    ('Issue', 'Issue'),
    ('Feature', 'Feature'),
    ('Suggestion', 'Suggestion'),
    ('Improvement', 'Improvement'),
    ('Other', 'Other')
]

USER_TYPE = (
    ('EMPLOYEE', 'Employee'),
    ('CONSULTANT', 'Consultant'),
    ('OWNER', 'Owner'),
    ('WRONG', 'Wrong'))


class Issues(TimeStampedModel):
    issue_owner = models.ForeignKey(USER_MODEL, related_name='issue_owner')
    issue_no = models.CharField(max_length = 500, null = True, blank = True)
    title = models.CharField(max_length=200, blank=True, null=True)
    owner_phone_number = models.CharField(max_length=25,blank=True, null=True)
    assigned_to_user = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='assigned_to_user')
    description = HTMLField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255, default='Open')
    issue_priority = models.CharField(choices=PRIORITY_CHOICES, max_length=255, default='None')
    classification = models.CharField(choices=CLASSIFICATION_CHOICES, max_length=255, null=True, blank=True)
    owner_role = models.CharField(choices=USER_TYPE, max_length=255, null=True, blank=True)
    snapshot = models.FileField(upload_to=get_attachment_file_path, max_length=500, null=True,blank=True, verbose_name="snapshot")
    due_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.issue_no:
            self.issue_no = increment_issue_number()
        if self.pk is not None:
            orig = Issues.objects.get(pk=self.pk)
            tenant = connection.get_tenant()
            url = tenant.domain_url
            link = "http://" + url + "/api/issue-details/" + str(self.id)
            if not orig.assigned_to_user and self.assigned_to_user:
                context = {"type":"Issue_Assigned", "template":"IssueAssigned", "link":link, "issue_no": self.issue_no, "issue_title":self.title, "descrption":self.description, "created_by":self.issue_owner.username, "priority":self.issue_priority, "classification":self.classification, "assigned_to":self.assigned_to_user.username, "email_to":self.assigned_to_user.email, "created_at":self.created}
                send_mail_data(context)
            elif orig.assigned_to_user:
                    if orig.assigned_to_user != self.assigned_to_user:
                        context = {"type":"Issue_Assigned", "template":"IssueAssigned", "link":link, "issue_no": self.issue_no, "issue_title":self.title, "descrption":self.description, "created_by":self.issue_owner.username, "priority":self.issue_priority, "classification":self.classification, "assigned_to":self.assigned_to_user.username, "email_to":self.assigned_to_user.email, "created_at":self.created}
                        send_mail_data(context)
        super(Issues, self).save(*args, **kwargs)

