from . import *

DEBUG = False
TEMPLATE_DEBUG = True

SECRET_KEY = '-~aO;| F;rE[??/w^zc4mh(9'

INSTALLED_APPS = [
    "products.apps.ProductsConfig",
    "accounts.apps.AccountsConfig",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # on utilise l'adaptateur postgresql
        "NAME": "purbeurre",  # le nom de notre base de donnees creee precedemment
        "USER": "postgres",  # attention : remplacez par votre nom d'utilisateur
        "PASSWORD": "",
        "HOST": "",
        "PORT": "127.0.0.1",
    }
}