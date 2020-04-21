from django.urls import path
from resturants.views import (
    ResturantListView,
    ResturantDetailView,
    ResturantCreateView,
)
app_name= "resturants"
urlpatterns = [
    path('', ResturantListView.as_view(), name="list"),
    path('create/', ResturantCreateView.as_view(), name="create"),
    path('<str:slug>/', ResturantDetailView.as_view(), name="detail"),

]

