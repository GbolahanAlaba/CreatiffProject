from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model



class Signup(AbstractUser):
    Image = models.TextField(default='', blank=True, null=True)
    Fullname = models.CharField(max_length=200, default='', blank=False, null=True)
    EmailAddress = models.EmailField(max_length=280, default='', null=False, unique=True, verbose_name='EmailAddress')
    Phonenumber = models.CharField(max_length=200, default='', blank=False, null=True)
    Address = models.CharField(max_length=300, default='', blank=False, null=True)
    Landmark = models.CharField(max_length=200, default='', blank=False, null=True)
    Label = models.CharField(max_length=100, default='', blank=False, null=True)
    Role = models.CharField(max_length=100, default='', blank=False, null=True)
    Identity = models.CharField(max_length=200, default='', blank=False, null=True)
    ID_Image = models.TextField(default='', blank=True, null=True)
    Document = models.TextField(default='', blank=True, null=True)
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    

    USERNAME_FIELD = "EmailAddress" 
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.Fullname + ' | ' + self.EmailAddress
    
    


# Create your models here.
