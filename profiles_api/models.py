from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles """

    def create_user(self, email, name, password=None):
        """ Add new user """
        if not email:
            raise ValueError('User must have an Email specified')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        """ Makes password encrpyted """
        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """Creates superuser """
        user = self.create_user(email, name, password)


        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()


    """ Default username is called USERNAME_FIELD, so we change it to allow login via emial """
    USERNAME_FIELD = 'email'
    """Specify Required fields """
    REQUIRED_FIELDS = ['name']

    """ Jeżeli funkcja jest w klasie to zawsze self w nawias """
    def get_full_name(self):
        """ Return name of user """
        return self.name

        """ UserProfile.get_full_name === nazwa uzytkownika """

    def get_short_name(self):
        return self.name

    def __str__(self):
        """ Return profile as string :D """
        return self.email
