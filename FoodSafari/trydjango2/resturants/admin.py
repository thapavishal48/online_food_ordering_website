from django.contrib import admin
from .models import ResturantLocation



# Register your models here.
class Resturant(admin.ModelAdmin):
    list_display = ('name', 'location', 'category','menus')             #it is used to display the database list in admin site

admin.site.register(ResturantLocation,Resturant)               #it is used to shown the database in admin site


