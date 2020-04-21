from django import forms

from .models import FoodItem
from resturants.models import ResturantLocation


class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = (
            "resturant",
            "name",
            "price",
            "category",
            "contents",
            "excludes",
            "public",
            "image"
        )

    def __init__(self, user, *args, **kwargs):      #it is used show that we can show only particular user resturant
        super().__init__(*args, **kwargs)
        self.user = user
        print(kwargs)
        self.fields["resturant"].queryset = ResturantLocation.objects.filter(owner=self.user)   #it is used so that  it only shows the resturant list which we made and  shoulnot display those resturant which are made by others
        #here field is resturant,name,content,exclude,public
        #here we are also filterin the queryset