
import usersData
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    acc_type = models.CharField(choices=(('Personal','Personal'),('Business','Business')),max_length=10,default='Personal') 
    bio = models.TextField(blank=False,default="bio")
    dob = models.DateField(blank=False)
    security_q = models.CharField(max_length=255,blank=False)
    security_ans = models.CharField(max_length=255,blank=False)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username+self.acc_type
class socialAcc(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    instagram = models.CharField(max_length=255,blank=True)
    twitter = models.CharField(max_length=255,blank=True)
    discord = models.CharField(max_length=255,blank=True)
    telegram = models.CharField(max_length=255,blank=True)
    facebook = models.CharField(max_length=255,blank=True)
    youtube = models.CharField(max_length=455,blank=True)
    gmail = models.CharField(max_length=255,blank=True)
    twitch = models.CharField(max_length=255,blank=True)
    phone_no = models.IntegerField(blank=True)
    snapchat = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return self.user.username+'SocialMedia'

class OTPModule(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.CharField(max_length=4,blank=False)
    valid = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'OTP for {self.user} at time {self.date_time}'