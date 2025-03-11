from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name= 'register'),
    path('profile/', views.user_profile, name = 'profile'),
    path('signin/', views.user_signin, name='login'),
]
