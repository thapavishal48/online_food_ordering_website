from django.core.exceptions import ValidationError


CATEGORIES = ["veg", "non-veg"]     #here in category we have to select only veg or no-veg when we make resturant name=create
def validate_resturant_name(resturant_name):
    if resturant_name == "create":      #when we put resturant name=create then is is not valid
        raise ValidationError(f"{resturant_name} cannot be used as a Resturant name.")


def validate_resturant_category(category):
    if category not in CATEGORIES:
        raise ValidationError(f"{category} is not a valid category. Use either of {CATEGORIES}")
