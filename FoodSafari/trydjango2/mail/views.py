from django.shortcuts import render
from django.http import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def sendmail(request):    #to send multiple emails
    html_content = "Thanks for ordering us !! We will contact you soon."
    notification = "Check your mail. Thanks for spending some quality time with the Web site today."
    send_mail('Send mail', html_content, settings.EMAIL_HOST_USER, ['thaparhombus@gmail.com','thapavishal48@gmail.com'], fail_silently=False)
    return HttpResponse('Check your mail')