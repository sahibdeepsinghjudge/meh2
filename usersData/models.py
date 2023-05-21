
import usersData
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    acc_type = models.CharField(choices=(('Personal','Personal'),('Business','Business')),max_length=10,default='Personal') 
    bio = models.TextField(blank=False,default="bio")
    profile_emoji = models.TextField(default="😊")
    dob = models.DateField(blank=True,null=True)
    security_q = models.CharField(max_length=255,blank=True,null=True)
    security_ans = models.CharField(max_length=255,blank=True,null=True)
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
    linkedin = models.CharField(max_length=255,blank=True)
    website = models.CharField(max_length=255,blank=True)
    phone_no = models.IntegerField(blank=True,default=0)
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

class ProfileVisits(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    raw_hits = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user} Visitor count' 
class ProfileHitsUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_hit = models.ForeignKey(User,on_delete=models.CASCADE,related_name='visitors')
    def __str__(self):
        return f'{self.user} Visitor details' 
class ProfileReactions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reaction = models.CharField(max_length=5)
    reactor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reactor')
    def __str__(self):
        return f'{self.user} Reaction book'

class verifiedAccounts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    def __str__(self):
        return f'{self.user.username} Verification'

class locationData(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    latitude = models.FloatField(default=0.00)
    longitude = models.FloatField(default=0.00)
    accuracy = models.FloatField(default=0.00)
    location_sharing = models.CharField(choices=(('off','off'),('on','on')),default='on',max_length=3)
    date = models.DateTimeField(auto_now=True)
    date_up = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username


class registerData(models.Model):
    email  = models.EmailField(blank=False)
    date_regitser  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class AccountSettings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    mehCard = models.CharField(choices=(('off','off'),('on','on')),default='on',max_length=3)
    eventNotifications = models.CharField(choices=(('off','off'),('on','on')),default='on',max_length=3)
    insights = models.CharField(choices=(('off','off'),('on','on')),default='on',max_length=3)

    def __str__(self):
        return "{}'s Account Setting".format(self.user) 

