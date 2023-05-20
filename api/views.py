from django.http.response import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from usersData.models import AccountSettings, ProfileVisits, info, locationData, registerData,socialAcc, verifiedAccounts,ProfileHitsUser
from .serializers import AccountSettingsSerializer, UserInfoSerializer,UserModelSerializer, UserRegisterDataSerializer,UserSocialAccSerializer,UserLocationDataSerializer
from django.contrib.auth.models import User

@api_view(['GET',"POST"])
def userData(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        
        Users = User.objects.all()
        User_serializer = UserModelSerializer(Users, many=True)
        Info = info.objects.all()
        info_serializer = UserInfoSerializer(Info, many=True)
        SocialAcc = socialAcc.objects.all()
        Social_serializer = UserSocialAccSerializer(SocialAcc, many=True)
        data = {
            'UserObj':User_serializer.data,
            'Social':Social_serializer.data,
            'Info':info_serializer.data
        }
        return Response(data)

@api_view(['GET'])
def registerCount(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        registers = registerData.objects.all()
        register_serializer = UserRegisterDataSerializer(registers, many=True)
        data = {
            'RegisterObj':register_serializer.data,
        }
        return Response(data)

#api call back home page status

@api_view(['GET', 'POST'])
def api_wayback_machine(request):
    if request.method == 'GET':
        data = {
            'usersUrl':'api/users/',
            '<username:>':'api/<str:username>',
        }
        return Response(data)

@api_view(['GET','POST'])
def UserDetails(request,username):
    
    if request.method == 'GET':
        try:
            Users = User.objects.get(username=username)
            User_serializer = UserModelSerializer(Users, many=False)
            acc_set = AccountSettings.objects.filter(user = Users.id)
            print(acc_set)
            acc_set_serializer = AccountSettingsSerializer(acc_set,many=True)
            try:
                Info = info.objects.get(user = Users.id)
                info_serializer = UserInfoSerializer(Info, many=False)
                SocialAcc = socialAcc.objects.get(user = Users.id)
             
                Social_serializer = UserSocialAccSerializer(SocialAcc, many=False)
                visits = ProfileVisits.objects.filter(user=Users.id).count()
                u_q_visits = ProfileHitsUser.objects.filter(user=Users.id).count()
                if request.user.id != Users.id:
                    vist = ProfileVisits.objects.create(user = Users)
                    vist.raw_hits = 1
                    vist.save()
                    if request.user.is_authenticated:
                        x = ProfileHitsUser.objects.get_or_create(user = Users,user_hit = request.user)
                        if not x:
                            x.save()
                verification = False
                
                try:
                    verifiedAccounts.objects.get(user=Users.id)
                    verification = True
                    data = {
                    'UserObj':User_serializer.data,
                    'Social':Social_serializer.data,
                    'Info':info_serializer.data,
                    
                    'Extra-Data':{
                        'Verified':verification,
                        'raw-count':visits,
                        'unique':u_q_visits,
                    },
                    'Settings':acc_set_serializer.data,
    
                    'status':200,
                    }
                    return Response(data)
                except:
                    verification= False
                    data = {
                    'UserObj':User_serializer.data,
                    'Social':Social_serializer.data,
                    'Info':info_serializer.data,

                    'Settings':acc_set_serializer.data,
                    
                    'Extra-Data':{
                        'Verified':verification,
                        'raw-count':visits,
                        'unique':u_q_visits
                    },
                        'status':200,
                    }
                    return Response(data)
                
                
            except :
                data ={
                    'status':420,
                    'details':'Incomplete Profile'
                }
                return Response(data)
        except:
               
                return Response(data = {'status':404,'details':'User does not exisit.'})


@api_view(['GET','POST'])
def LocationDetails(request,username):
    Users = User.objects.get(username=username)
    if request.method == 'GET':
                try:
                        location = locationData.objects.get(user = Users.id)
                        print("location",location)
                except:
                        location = locationData.objects.create(user = Users)
                        print("location",location)
                        location.save()
                Location_serializer = UserLocationDataSerializer(location, many=False)
                print(Location_serializer.data)
                return Response(Location_serializer.data)