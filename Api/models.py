from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from .manager import UserManager



class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=255,null=True,blank=True)
    email_verification_token = models.CharField(max_length=200,null=True,blank=True)
    forget_password_token = models.CharField(max_length=200,null=True,blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email 

class Student(models.Model):

    name = models.CharField(max_length=255,unique=True)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=255,unique=True)


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Book(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)

