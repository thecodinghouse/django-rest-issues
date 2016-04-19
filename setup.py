from distutils.core import setup
setup(
  name = 'django-rest-issues',
  packages = ['issues'], # this must be the same as the name above
  version = '1.2',
  description = 'Django rest issues is issue raising system. Here logged in users can rais the issues.',
  author = 'Gaurav Wagh',
  author_email = 'waghgaurav.g@gmail.com',
  url = 'https://github.com/tixdo/django-rest-issues', # use the URL to the github repo
  download_url = 'https://github.com/tixdo/django-rest-issues/tarball/0.1', # I'll explain this in a second
  install_requires=[
            "django-contrib-comments==1.6.1",
            "django-tinymce==2.2.0",
            "django-post-office==2.0.1",
            ],
  keywords = ['Django', 'Django-issues', 'python'], # arbitrary keywords
  classifiers = [],
)