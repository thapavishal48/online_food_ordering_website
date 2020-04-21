from django.urls import path
from django.contrib.auth.views import LogoutView

from userauth.views import SignUpView, UserProfileView, UserLoginView, UserProfileUpdateView
app_name= "userauth"
urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="/login/"), name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('user-profile/', UserProfileView.as_view(), name="profile"),
    path('user-profile/update/', UserProfileUpdateView.as_view(), name="update"),

]
