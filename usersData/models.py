
from typing import Iterable, Optional
import usersData
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

event_type = (('public','public'),('private','private'),('sale','sale'),('offer','offer'),('open','open'),('closed','closed'),('other','other'))


class info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    acc_type = models.CharField(choices=(('Personal','Personal'),('Business','Business')),max_length=10,default='Personal') 
    bio = models.TextField(blank=False,default="bio")
    profile_emoji = models.TextField(default="😊")
    dob = models.DateField(blank=True,null=True)
    security_q = models.CharField(max_length=255,blank=True,null=True)
    security_ans = models.CharField(max_length=255,blank=True,null=True)
    business_linked = models.BooleanField(default=False)
    business_linked_account = models.ForeignKey("BusinessDetails",on_delete=models.CASCADE,blank=True,null=True)
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
   #github = models.CharField(max_length=255,blank=True)

    def return_connected_accounts(self):
        return {
            'instagram':self.instagram,
            'twitter':self.twitter,
            'discord':self.discord,
            'telegram':self.telegram,
            'facebook':self.facebook,
            'youtube':self.youtube,
            'gmail':self.gmail,
            'twitch':self.twitch,
            'linkedin':self.linkedin,
            'website':self.website,
            'phone_no':self.phone_no,
            'snapchat':self.snapchat,
        }

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
    


class Events(models.Model):
    name = models.CharField(max_length=255,blank=False)
    description = models.TextField(blank=False)
    event_date = models.DateField(blank=False)
    start_time = models.CharField(blank=False,max_length=10,default="10:00 AM")
    end_time = models.CharField(blank=False,max_length=10,default="12:00 PM")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    map_range = models.IntegerField(blank=False,default=50) #meters
    latitude = models.CharField(max_length=255,blank=False)
    longitude = models.CharField(max_length=255,blank=False,default=0.00)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    event_type = models.CharField(choices=event_type,default='public',max_length=10)

    def __str__(self) -> str:
        return self.name
    
    def save(self,*args,**kwargs):
        self.map_range = self.map_range*1000 #converting to meters
        return super().save(*args,**kwargs)
    
class BusinessDetails(models.Model):
    business_name = models.CharField(max_length=255,blank=False)
    business_description = models.TextField(blank=False)
    business_type = models.CharField(max_length=255,blank=False)
    business_location = models.CharField(max_length=255,blank=False)
    business_website = models.CharField(max_length=255,blank=False)
    business_email = models.EmailField(blank=False)
    business_phone = models.IntegerField(blank=False)
    #business_logo = models.ImageField(upload_to='business_logo',blank=False)

    def __str__(self) -> str:
        return self.business_name