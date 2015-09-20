### Rename your project_name
#### Manage.py
#### Change the settings according to the your development, staging and production server
Change the environment during deployment as staging or production
```manage.py
environment = "development" # staging or production

if environment == "production":
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings_production")
  elif environment == "staging":
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings_staging")
  elif environment == "development":
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings_development")

```

#### Settings.py
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

##### Additional details
To create a very secure and secret key, please check the documentation here    
https://gist.github.com/ndarville/3452907
