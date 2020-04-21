#usely used in url browsers
import random
import string
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)   #slugify: replace space with - sign

    Klass = instance.__class__      #getting the class of instance nad we are getting ResturatLocation class
    qs_exists = Klass.objects.filter(slug=slug).exists()        #first slug is from mulde.py slug and the seccond one is local variable and we can change as slugg also and other name
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(       #used to generate random character in slug if there are same name and it generate uniquely
            slug=slug,
            randstr=random_string_generator(size=4)     #it will add the ranadom slug character of 4 letters as size is 4
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
