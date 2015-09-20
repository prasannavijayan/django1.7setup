#!/usr/bin/env python
import os
import sys

# Please change the environment during deployment
environment = "development"

if __name__ == "__main__":

    if environment == "production":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings_production")
    elif environment == "staging":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings_staging")
    elif environment == "development":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings_development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
