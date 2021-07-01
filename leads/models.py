from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name}"


class Lead(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
    organization = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', related_name='leads', on_delete=models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    organization = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.user.first_name } { self.user.last_name }"
    
class Category(models.Model):
    name = models.CharField(max_length = 50)
    organization = models.ForeignKey('UserProfile',on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)

