from . import *
"""import django

django.setup()

DEBUG = False
TEMPLATE_DEBUG = True

SECRET_KEY = '-~aO;| F;rE[??/w^zc4mh(9'"""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # on utilise l'adaptateur postgresql
        "NAME": "",  # le nom de notre base de donnees creee precedemment
        "USER": "postgres",  # attention : remplacez par votre nom d'utilisateur
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}