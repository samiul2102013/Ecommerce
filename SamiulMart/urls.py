from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('store/', include('store.urls')),
    #path('category/', include('category.urls')),
]
