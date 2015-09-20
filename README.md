#### Rename your project_name
### Manage.py
Change the project_name to   
```manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
```
to   
```manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<your_project_name>.settings")
```
### Settings.py
Change the project_name to
```variables
ROOT_URLCONF = 'project_name.urls'

WSGI_APPLICATION = 'project_name.wsgi.application'
```
to   
```variables
ROOT_URLCONF = '<your_project_name>.urls'

WSGI_APPLICATION = '<your_project_name>.wsgi.application'
```
