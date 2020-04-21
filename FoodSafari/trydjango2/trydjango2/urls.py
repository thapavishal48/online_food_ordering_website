# """trydjango2 URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # from django.contrib import admin
# # from django.urls import path
# # #from resturants.views import home_view,hotel,contact
# # from resturants.views import ContactView    #home URL
# #
# #
# # urlpatterns = [                            #endpoints
# #     path('admin/', admin.site.urls),
# #     path("home/",home_view),             #to open home path.....first parameter as the endpoint and the second parameter as the function
# #     path("hotel/",hotel),
# #     path("contact/",ContactView.as_view()),#as_view() make the class callable but generally class is not callabe
# # ]
#
# from django.contrib import admin
# from django.urls import path
# from resturants.views import ContactView
# from resturants.views import (
#     resturant_list,
#     ResturantListView,
#     ResturantDetailView,
#     ResturantCreateView
# )
# from django.views.generic import TemplateView
# from userauth.views import SignUpView, UserProfileView, UserLoginView, UserProfileUpdateView
# from django.contrib.auth.views import LogoutView
#
#
# #from userauth.views import SignUpView,CustomLoginView
#
#
# urlpatterns = [
#                                                     #path('endpoints/, function/class())
#     path('admin/', admin.site.urls),
#     path('login/', UserLoginView.as_view()),
#     path('signup/', SignUpView.as_view()),
#     path('logout/', LogoutView.as_view(next_page="/login/")),       #it is used to make logout
#     path('user-profile/', UserProfileView.as_view()),
#     path('user-profile/update/', UserProfileUpdateView.as_view()),
#
#     #path('users/login', CustomLoginView.as_view()),
#     #path('users/signup', SignUpView.as_view()),
#
#     path("contact/",ContactView.as_view()),
#
#     #path('resturants/',resturant_list),
#     path('resturants/', ResturantListView.as_view()),
#
#     path('resturants/create/', ResturantCreateView.as_view()),
#
#     #path('resturants/create/', resturant_createview),
#
#     #path('resturants/<str:slug>/', ResturantListView.as_view()),
#     path('resturants/<str:slug>/', ResturantDetailView.as_view()),
#
#     #path('resturants/<int:rest_id>/',ResturantDetailView.as_view()),
#
#     path('home/', TemplateView.as_view(template_name="home.html")),
#     path('hotel/', TemplateView.as_view(template_name="hotel.html")),
#
#     #path('resturants/veg', VegResturantListView.as_view()),
#     #path('resturants/nonveg', NonVegResturantListView.as_view()),
#
#     #<data_type :var_name>  #to declare varibale inside endpoints
#
# ]

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from resturants.views import  HomeTemplateView
#from  mail.views import sendmail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("userauth.urls", namespace="userauth")),        #namespace is  used when we need to insert the all userauth related url in trydjango2
    path('resturants/', include("resturants.urls", namespace="resturants")),
    path('items/', include("fooditem.urls", namespace="fooditem")),
    path('order/', include("orderitem.urls", namespace="orderitem")),


    path('home/', HomeTemplateView.as_view(),name="home"),

    path('', include('sendemail.urls')),
#path('notify/',sendmail),       #used to send email
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)