# users/views.py
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, UpdateView
from django.shortcuts import render, get_object_or_404

from .forms import CustomUserCreationForm,CustomUserUpdateForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):                #it is used to make the signup page
    form_class = CustomUserCreationForm
    template_name = 'userauth/signup.html'
    def get_success_url(self):
        return reverse_lazy("userauth:login")


class UserLoginView(LoginView):                  #it is used to make log_in page
    template_name = 'userauth/login.html'
    redirect_authenticated_user=True
    def get_success_url(self):                      #it is used to open the next= value like we created in resturants/create
        next=(self.request.GET.get('next'))
        if next:
            return next
        else:
            return reverse_lazy("userauth:profile")     #it is bascially used during making dynamic url,when we change anything in backend in url,it is not related to frontend,we dynamically defined url at that time , and when we change name of url in backend then we donot need to make any sort of chnages in frontend .
                                                        # eg_>/logggginn/ _>name="login-->{% url:login %} then in reverse_lazy is goes {% url:login %}->name="login->/logggginn/ and make dynamic url


class UserProfileView(LoginRequiredMixin,DetailView):              #it is used to give the detail of user
    login_url = reverse_lazy("userauth:login")                       #LoginRequiredMixin Verify that the current user is authenticated.
    template_name = "userauth/profile.html"

    def get_object(self, queryset=None):
        username = self.request.user.get_username()
        user_detail = get_object_or_404(CustomUser, username=username)
        return user_detail

class UserProfileUpdateView(LoginRequiredMixin,UpdateView):        #it is used to update the detail of user page
    login_url = reverse_lazy("userauth:login")
    form_class = CustomUserUpdateForm
    template_name = "userauth/update.html"

    def get_object(self, queryset=None):
        username = self.request.user.get_username()
        user_detail = get_object_or_404(CustomUser, username=username) #if the username matches then only user detail will be displayed otherwise 404 warning occur,
                                                                        #and if the user is unauthorized is shows 404 error
        return user_detail

    def get_success_url(self):
        return reverse_lazy("userauth:profile")

#in utilis we add those thing that can be used at any place
#in services we add those which perform specific function only