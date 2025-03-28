from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart, name = 'cart'),
    path('<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('delete/<int:product_id>/', views.delete_cart, name='delete_cart'),
]
