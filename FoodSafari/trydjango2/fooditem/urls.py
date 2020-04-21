from django.urls import path


from fooditem.views import (
    FoodItemCreateView,
    FoodItemListView,
    FoodItemDetailView,
    FoodItemUpdateView,

)



app_name = "fooditem"

urlpatterns = [
    path('', FoodItemListView.as_view(), name="list"),


    path('<str:pk>/', FoodItemDetailView.as_view(), name="detail"),
    #path('<str:pk>/update/', FoodItemUpdateView.as_view(), name="update"),
    # path('create/', FoodItemCreateView.as_view(), name="create"),


]



