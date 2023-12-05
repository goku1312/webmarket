from django.db import models
from django.contrib.auth.models import AbstractUser

from django_otp.plugins.otp_totp.models import TOTPDevice
# Create your models here.



class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username


class register(models.Model):
        name = models.CharField(max_length=50)
        phone = models.IntegerField()
        email = models.EmailField()
        state = models.CharField(max_length=30)
          



class Logins(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username
    


class PremiumCard(models.Model):
    temp_img=models.ImageField(upload_to="temp_meadia")
    temp_file=models.FileField(upload_to="templates")
    creator_name=models.CharField( max_length=50)
    model_name=models.CharField(max_length=50,blank=True)
    category_name=models.CharField(default="Premium Templates",max_length=50)
    price=models.IntegerField(default=399)

    def __str__(self):
            return self.creator_name
    
class TemplateCard(models.Model):
    temp_img=models.ImageField(upload_to="temp_meadia")
    temp_file=models.FileField(upload_to="templates")
    creator_name=models.CharField( max_length=50)
    model_name=models.CharField(max_length=50,blank=True)
    category_name=models.CharField(default="Premium Templates",max_length=50)
    price=models.IntegerField(default=199)

    def __str__(self):
            return self.creator_name
    


    # models.py

