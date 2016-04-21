## django-rest-issues
Django-rest-issues is issue raising system for django rest-framework. This package helps you to add the ticketing system to your application. If user has any issues or suggestions he can log that here. We can use this issue tracking in web apps, android or ios apps. While creating issues user needs to be logged in.

## Installation
1. 
`pip install django-rest-issues`

 Include "issues" to your install apps and run the migrations.

 Inside settings.py file include following settings

`DOMAIN_URL="www.xyz.com/admin"`

include the domain url till the admin

`FROM_EMAIL="abc@gmai.com"`

FROM_EMAIL is email address from which emails will get sent.

`EMAIL_TO=["xyz@gmail.com","pqr@gmail.com"]`

EMAIL_TO is list of emails which will get the email alerts after issues created.

2.
Or you can download zip file and copy pest issues app to your project. Then run the migrations.

**For sending mail create post office templates in admin.**

1. template Name "IssueCreated"

  Subject "New issue created on your project name"

  template "post-office-templates/IssueCreated.html"


2. template Name "IssueAssigned"

  Subject "Issue assigned on your project name"

  template "post-office-templates/IssueAssigned.html"

_Pest templates html code to HTML content inside admin_

_**Use the exact same template names mentioned above**_

**Create two groups in django admin groups table**

1. Administrator
2. Tickets

for Administrator group give all issues app related permissions EX. can add issue, can change issue etc

for Tickets group give only one issues app related permissions i.e. "can change issue"

Add the users to Administrator group who has the authority to assign issues to other users.

And add users to Tickets group who has the authority to resolve issues. (The users who are actually resolves the issue )

At least one administrator and one tickets group user is required.


See the [Doc's](http://tixdo.github.io/django-rest-issues/)

## API'S

### /issue/issues_by_user/
Get's the list of issues created by the user.
* param: None

_This api gives the list of issues created by current logged in user._

### /issue/issues_by_status/
Get's the list of issues for particular status.
* param: status i.e. status=open

_result: List of all issues who's status is open_

### /issue/issues_by_priority/
Get's the list of issues for particular priority.
* param: priority i.e. status=high

_result: List of all issues who's priority is high_

### /issue/issues_by_classification/
Get's the list of issues for particular classification.
* param: classification i.e. classification=issue

_result: List of all issues who's classification is issue_

### /issue/issues_by_status_and_user/
Get's the list of issues for current user and provided status.
* param: status i.e. status=open

_result: List of all issues created by current user who's status is open_

### /issue/issues_by_priority_and_user/
Get's the list of issues for current user and provided priority.
* param: priority i.e. priority=high

_result: List of all issues created by current user who's priority is high_

### /issue/issues_by_classification_and_user/
Get's the list of issues for current user and provided classification.
* param: classification i.e. classification=issue

_result: List of all issues created by current user who's classification is high._
