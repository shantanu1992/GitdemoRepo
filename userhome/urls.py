from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='userhome'),
    path('userdetails', views.userdetails),
    path('registration', views.registration, name='registration'),
    path('login', views.loginuser, name='loginuser'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('contact_card', views.contact_card, name='contact_card'),
]