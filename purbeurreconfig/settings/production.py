from . import *

SECRET_KEY = '-~aO;| F;rE[??/w^zcumh(9'
DEBUG = False
ALLOWED_HOSTS = ['142.93.71.71']

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
