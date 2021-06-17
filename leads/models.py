from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


# Create your models here.
class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.user.first_name } { self.user.last_name }"
