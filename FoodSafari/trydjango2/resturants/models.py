from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_resturant_category, validate_resturant_name
from userauth.models import CustomUser

# Create your models here.
class ResturantLocation(models.Model):      # we are making the resturant related database in table
    name=models.CharField(max_length=120,validators=[validate_resturant_name])      #it is used to check whether the resturant name is "create" or not, if yes then it is not valid
    location=models.CharField(max_length=120,null=True,blank=True)     #null and blank: if we leave blank then it work as it is True

    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_resturant_category])
    owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)      #CASCADE: it used to delete the entire related data of that user in database,when we delete that user


    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    menus = models.CharField(max_length=120, null=True, blank=True)
    slug=models.SlugField(null=True,blank=True)     #it is used to make the browser address beautiful

    def __str__(self):
        return self.name


def pre_save_receiver(sender, instance, *args, **kwargs):
    print("saving {}".format(instance))         #instance means object like Bota resturant,name,location,category etc
    if not instance.slug:           #it adds something into the slug it is not wriiten in database
        instance.slug = unique_slug_generator(instance)


def post_save_receiver(sender, instance, created, *args, **kwargs):
    print("saved {}".format(created))

pre_save.connect(pre_save_receiver, sender=ResturantLocation)

post_save.connect(post_save_receiver, sender=ResturantLocation)




