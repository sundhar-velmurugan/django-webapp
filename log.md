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
- Static files such as CSS, JS are put inside the *app-name* -> static -> *app-name* directory in the application
- Static files can be loaded into the template afte adding `{% load static %}` in the top of the template
- Urls in template can be referenced by url name instead of hardcoding


### Admin page
- Added admin credentials in *auth_user* table
- `python manage.py migrate` to run migrations - this will create *auth_user* table
- `python manage.py createsuperuser` to create super user
  - my credentials: *sundhar*
- Admin page can be accessed in `http://localhost:8000/admin/`

### Database and migrations
- Database schema is created in `models.py`
- `python manage.py makemigrations` makes files that has instructions on migrations
- `python manage.py sqlmigrate <app-name> <migration-id>` - to view the SQL code for the migrations
- `python manage.py migrate` to run migrations
- Migrations are an easy way to change database schema
- Models of each app needs to be registed in `admin.py` to view in the admin page

### User Registration
- Created users app using `python manage.py startapp users`
- Added the users app to the INSTALLED_APPS list in settings.py
- Flash message [one time notification message] is sent after registration
- Created a seperate RegistrationForm from UserCreationForm with email field
- Registration form is styled using crispy forms

### Login and logout
- View can be made private using inbuild **login_required** decorator

### User Profile and Picture
- User and Profile model is one to one related
- Media root: location where the uploaded files are in the file system
- Media url: access the media through browser
