from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart_summary,name='cart_summary'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
]