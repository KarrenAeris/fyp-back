from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254, unique=True, verbose_name='Email')
    username = models.CharField(max_length=255, verbose_name='Username', null=True, blank=True)
    # delivary_address = models.CharField(max_length=254, verbose_name='Delivary Address')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]