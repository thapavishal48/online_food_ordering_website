from django.urls import path
from orderitem.views import FoodOrderedCreateView


app_name = "orderitem"

urlpatterns = [
    path('create/', FoodOrderedCreateView.as_view(), name="order"),


]
