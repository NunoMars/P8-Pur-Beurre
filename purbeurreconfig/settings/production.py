from . import *

SECRET_KEY = '\\\ta(xZQ;xUIly1X@IGT:4re$'
DEBUG = False
ALLOWED_HOSTS = ['104.236.42.41']

INSTALLED_APPS += [
    'django_crontab',
]    

CRONJOBS = [
    ('* 23 * * 7', 'django.core.management.call_command', ['insertdata']),
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # on utilise l'adaptateur postgresql
        "NAME": "PurBeurre",  # le nom de notre base de donnees creee precedemment
        "USER": "Remi",  # attention : remplacez par votre nom d'utilisateur
        "PASSWORD": "remisansfamille",
        "HOST": "",
        "PORT": "5432",
    }
}
