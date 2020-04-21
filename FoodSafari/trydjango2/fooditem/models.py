from django.db import models
from userauth.models import CustomUser
from resturants.models import ResturantLocation

a = list()

# Create your models here.
class FoodItem(models.Model):
    # associations
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resturant = models.ForeignKey(ResturantLocation, on_delete=models.CASCADE)

    # FoodItems data
    name = models.CharField(max_length=100)                         #food item name
    category = models.CharField(max_length=100,null=True,blank=True)
    price=models.CharField(max_length=120,null=True,blank=True)
    contents = models.TextField(help_text='seperate by comma')
    excludes = models.TextField(help_text='seperate by comma', blank=True, null=True)   #
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="profile_image",blank=True,null=True)

    def __str__(self):
        return self.user

    class Meta:     #Meta is like class description
        ordering = ["-updated", "-timestamp"]

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{__class__.__name__}({self.name} <{self.user!r}> <{self.resturant!r}>)"

    def get_contents(self):
        return self.contents.split(",")     #split changes to list

    def get_excludes(self):
        return self.excludes.split(",")
