from django import forms
from .models import FoodOrdered

class FoodOrderedForm(forms.ModelForm):
    class Meta:
        model=FoodOrdered
        fields=[
            "Resturant_name",
            "Food_order",
            "Location",
            "Category",
            "Owner",
            "Contact_no",
            "Gmail",
        ]
