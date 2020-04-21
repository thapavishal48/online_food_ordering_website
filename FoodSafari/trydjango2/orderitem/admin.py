from django.contrib import admin
from .models import FoodOrdered


# Register your models here.
class Food(admin.ModelAdmin):
    list_display = (
        "Resturant_name",
            "Food_order",
            "Location",
            "Category",
            "Owner",
            "Contact_no",
            "Gmail",

        )
admin.site.register(FoodOrdered,Food)



