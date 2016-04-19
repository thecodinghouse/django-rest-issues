## django-rest-tickets
Django-rest-ticket is ticket or issue raising system for django rest-framework. This package helps you to add the ticketing system to your application. If user has any issues or suggestions he can log that here. We can use this issue tracking in web apps, android or ios apps. While creating issues user needs to be logged in.

## Installation
1. 
`pip install django-rest-tickets`
Include "issues" to your install apps and run the migrations.

2.
Or you can download zip file and copy pest issues app to your project. Then run the migrations.

## API'S

### /issue/issues_by_user/
Get's the list of issues created by the user.
* param: None
> This api gives the list of issues created by current logged in user.

### /issue/issues_by_status/
Get's the list of issues for particular status.
* param: status i.e. status=open
> result: List of all issues who's status is open

### /issue/issues_by_priority/
Get's the list of issues for particular priority.
* param: priority i.e. status=high
> result: List of all issues who's priority is high

### /issue/issues_by_classification/
Get's the list of issues for particular classification.
* param: classification i.e. classification=issue
> result: List of all issues who's classification is issue

### /issue/issues_by_status_and_user/
Get's the list of issues for current user and provided status.
* param: status i.e. status=open
> result: List of all issues created by current user who's status is open

### /issue/issues_by_priority_and_user/
Get's the list of issues for current user and provided priority.
* param: priority i.e. priority=high
> result: List of all issues created by current user who's priority is high

### /issue/issues_by_classification_and_user/
Get's the list of issues for current user and provided classification.
* param: classification i.e. classification=issue
> result: List of all issues created by current user who's classification is high.
