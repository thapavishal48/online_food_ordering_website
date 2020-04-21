from django.db import models
from userauth.models import CustomUser


# Create your models here.

class FoodOrdered(models.Model):
    Resturant_name=models.CharField(max_length=120,null=True,blank=True)
    Food_order=models.CharField(max_length=120,null=True,blank=True)
    Location=models.CharField(max_length=120,null=True,blank=True)
    Category = models.CharField(max_length=120, null=True, blank=True,)
    Owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    Contact_no = models.CharField(max_length=120, null=True, blank=True)
    Gmail = models.CharField(max_length=120, null=True, blank=True)

    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)








