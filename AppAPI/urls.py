from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('api/get_user/', views.get_user, name='get_user'),
    path('api/signup_user/', views.signup_user, name='signup_user'),
    path('api/signin_user/', views.signin_user, name='signin_user'),
    path('api/logout/', knox_views.LogoutView.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view()),
    
]