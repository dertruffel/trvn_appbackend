import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManagerActive, UserManager
from django.db import models

class BaseUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    password = models.TextField()
    email = models.TextField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.email

    class Meta:
        abstract = True
        app_label = 'accounts_base'

class User(BaseUser,
    models.Model):
    jwt_secret = models.UUIDField(
        default=uuid.uuid4,
        help_text='The field is used by REST framework to create jwt token.',
    )
    all_objects = UserManager()
    objects = UserManagerActive()
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        if self.username is not None:
            return self.username
        else:
            return self.email

    class Meta:
        app_label = 'accounts'

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('User', related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.name