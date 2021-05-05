from phishtray.settings import *  # noqa

"""
Django settings for phishtray project travis CI.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "test",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "3306",
    }
}