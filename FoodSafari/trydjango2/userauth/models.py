from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):     #it uses the already defined filled like name,email,category and we only abstract
    location=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.username
