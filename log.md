### Getting Started
- Created a Django project
`django-admin startproject django_project`

### Application and Routes
- creating a blog app
`python manage.py startapp blog`
- created views and routes for blog app

### Templates
- Created template files in *app-name* -> templates -> *app-name* directory
- Added the Blog app to the Django project
  - in `settings.py` file added `blog.apps.BlogConfig` under *INSTALLED_APPS*
  - Django uses the INSTALLED_APPS to search for templates and models
- To return templates as response
  - django.shortcuts -> render method is used
  - render returns a HttpResponse with HTML from template
- Render method has 3 arguments
  - request object
  - path to the template, relative to templates directory in the app
  - data
- Avoided repeating HTML using Template Inheritance