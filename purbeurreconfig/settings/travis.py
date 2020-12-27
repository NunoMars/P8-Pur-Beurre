SECRET_KEY = '-~aO;| F;rE[??/w^zc4mh(9'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # on utilise l'adaptateur postgresql
        "NAME": "purbeurre",  # le nom de notre base de donnees creee precedemment
        "USER": "postgres",  # attention : remplacez par votre nom d'utilisateur
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}