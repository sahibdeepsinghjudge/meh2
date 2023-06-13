from django.db.models import fields
from rest_framework import serializers
from usersData.models import AccountSettings, BusinessDetails, Events, info, socialAcc,locationData,registerData
from django.contrib.auth.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields = '__all__'

class UserSocialAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = socialAcc
        fields = '__all__'

class UserLocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = locationData
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','date_joined','last_login']

class UserRegisterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = registerData
        fields = '__all__'


class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSettings
        fields = '__all__'

class BusinessDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDetails
        fields = '__all__'
    
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'