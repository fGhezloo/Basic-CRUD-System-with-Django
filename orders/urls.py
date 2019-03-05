from django.urls import path
from .views import OrdersView


app_name = "orders"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('orders/', OrdersView.as_view()),
    path('orders/<int:pk>', OrdersView.as_view()),
]