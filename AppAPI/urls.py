from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
    path('api/subscribe/', views.Subscribers, name='subscribe'), #subscription link
    path('api/signup_user/', views.signup_user, name='signup_user'), #signup link
    path('api/signin_user/', views.signin_user, name='signin_user'), #sigin link
    path('api/get_user/', views.get_user, name='get_user'), #get user link
    path('api/logout/', knox_views.LogoutView.as_view()), #logout link
    path('api/logoutall/', knox_views.LogoutAllView.as_view()), #logout all link
    
]