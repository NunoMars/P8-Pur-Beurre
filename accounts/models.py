import time
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staf, is_superuser, **extra_fields):
        """
        Creates and saves a User with teh given email and password.

        """
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)

        if not email:
            raise ValueError('Vous devez renseigner un email!')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staf=is_staf,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'second_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % (self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.second_name)
        return full_name.strip()
