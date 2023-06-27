from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('api/signin_user/', views.signin_user, name='signin_user'),
    path('api/get_user/', views.get_user, name='get_user'),
    path('api/signup_user/', views.signup_user, name='signup_user'),
    
]