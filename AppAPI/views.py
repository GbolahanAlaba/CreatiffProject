from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.permissions import IsAuthenticated   
from . serializers import *

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@api_view(['POST'])
def signin_user(request):

    # user = get_user_model().objects.filter()

    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    
    _, token = AuthToken.objects.create(user)

    return Response({

        'user_info':{
            'id': user.id,
            'image': user.Image,
            'Fullname': user.Fullname,
            'EmailAddress': user.EmailAddress,
            'Phonenumber': user.Phonenumber
        },
    'token': token
    }, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:

        return Response({
            'user_info':{
                'id': user.id,
                'Fullname': user.Fullname,
                'EmailAddress': user.EmailAddress,
                'Time': user.Timestamp
            },
        })
    
    else:
        return Response({'Error!': 'User not logged in'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def signup_user(request):

    if request.method == 'GET':
        sub = get_user_model().objects.all()
        serializer = Signup_userSerializer(sub, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method =='POST':

        serializer = Signup_userSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        _, token = AuthToken.objects.create(user)

        return Response({
            'user_info':{
                'id': user.id,
                'username': user.username,
                'EmailAddress': user.EmailAddress
            },
        'token': token
        }, status=status.HTTP_201_CREATED)
    
    else:
        return Response()


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        user = get_user_model().objects.all()
        [reset_password_token.user.email]
    )



 # Create your views here.
