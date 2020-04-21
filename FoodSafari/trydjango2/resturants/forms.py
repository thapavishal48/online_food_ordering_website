from django import forms
from .models import ResturantLocation


class ResturantLocationModelForm(forms.ModelForm):  #advantage-dynamic,consistency and it will do the same function as ResturantCreateForm
    class Meta:                 #it is going to define the behaviour of the ResturantLocation model form
        model=ResturantLocation
        #fileds="__all__"       # to include all the field
        fields=[                #to include particular field
            "name",
            "location",
            "category",
            "menus",
            "slug"
        ]
