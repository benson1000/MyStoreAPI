from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class Permission(models.Model):
    name = models.CharField(max_length=255)


class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField(Permission)


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.CharField(max_length=255)


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
