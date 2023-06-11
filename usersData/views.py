from django.contrib.auth import models
import usersData
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import AccountSettings, OTPModule, ProfileHitsUser, ProfileVisits, info, locationData, registerData, socialAcc, verifiedAccounts
import pyqrcode
from django.core.mail import BadHeaderError, message, send_mass_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context, context
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from math import sin, cos, sqrt, atan2, radians
import png
import random
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, time, timedelta, timezone
from pyqrcode import QRCode
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def registerUser(request):
    return HttpResponse('Response:200')

def removeOldOtp():
        otpmods = OTPModule.objects.filter(valid = False)
        otpmods.delete()


def validateForm1(request):
    if request.method=='POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        username = username.replace(" ", "")
        try:
            user = User.objects.filter(email=email)
            mail = User.objects.filter(username=username)
            pswd = request.POST.get('pswd')
            if user or mail:
                data = {
                    'validated':['true'],
                    'no_account':['false']
                }

                return JsonResponse(data)
            else:
                '''asdfhb'''
                user_create=User.objects.create(email=email,username=username)
                user_create.set_password(pswd)
                user_create.save()
                data = {
                    'validated':['true'],
                    'no_account':['true']
                }
                if request.POST:
                    user = authenticate(username=username, password=pswd)
                    if user is not None:
                        if user.is_active:
                            login(request, user)

                dob = request.POST.get('dob')
                secu_q = request.POST.get('ques')
                ans = request.POST.get('ans')
                emoji = request.POST.get('emoji')

                uid = User.objects.get(username=username)
                acc = AccountSettings.objects.create(user = uid)
                socialAccObj = socialAcc.objects.create(user = uid)
                socialAccObj.save()
                acc.save()
                infoObj = info.objects.create(user = uid)
                infoObj.save()
                return JsonResponse(data)
        except:
            user =False
@csrf_exempt
def postInfo(request):
    if request.method=='POST':
        acc_type = request.POST.get('acc_type')
        dob = request.POST.get('dob')
        bio = request.POST.get('bio')
        secu_q = request.POST.get('ques')
        ans = request.POST.get('ans')
        uid = User.objects.get(username=request.user.username)
        infoObj = info.objects.create(user = uid,acc_type=acc_type,bio=bio,dob=dob,security_q=secu_q,security_ans=ans)
        infoObj.save()
        return HttpResponse('created')
    else:
        return JsonResponse({"status":500,'data':"Not created not POST request"})
    

@csrf_exempt
def postInfoAccs(request):
    if request.method=='POST':
        insta = request.POST.get('insta')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        youtube = request.POST.get('youtube')
        snapchat = request.POST.get('snap')
        twitch = request.POST.get('twitch')
        gmail = request.POST.get('gmail')
        phn = request.POST.get('phone')
        telegram = request.POST.get('telegram')
        discordX = request.POST.get('ds')

        if discordX == None:
            discordX = ''
        if telegram == None:
            telegram = ''

        if  gmail or phn:
            if len(phn)==0:
                    phn = 0
            if len(gmail) ==0:
                    userObj = User.objects.get(username = request.user.username)
                    gmail = userObj.email
            user_create=socialAcc.objects.create(user = request.user,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,phone_no=phn,gmail=gmail,discord=discordX)
            user_create.save()
        else:

            user_create=socialAcc.objects.create(user = request.user,gmail='',phone_no=0,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,discord=discordX)
            user_create.save()
        return redirect('/')

def loginApi(request):
    if request.user.is_authenticated:
        logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('success')
        else:
            return HttpResponse('faliure')
    else:
        return HttpResponse('denied')

def logoutApi(request):
    logout(request)
    return redirect('/')

def profile(request):
    removeOldOtp()
    return render(request,'home/profile.html')

def autoVerifyUser(username):
    userObj = User.objects.get(username = username)
    try:
        verifiedAccounts.objects.get(user=userObj)
    except:
        unique_vist_count = ProfileHitsUser.objects.filter(user = userObj.id).count()
        if unique_vist_count>=100:
                ver = verifiedAccounts.objects.create(user = userObj)
                ver.save()
    return True


def returnUserData(request,username):
    removeOldOtp()
    autoVerifyUser(username)
    userObj = User.objects.get(username=username)
    x = request.user.username
    if  username != x:
        vist = ProfileVisits.objects.create(user = userObj)
        vist.raw_hits = 1
        vist.save()
        if request.user.is_authenticated:
            x = ProfileHitsUser.objects.get_or_create(user = userObj,user_hit = request.user)
            if not x:
                x.save()

    userdata = User.objects.get(username = username)
    verification = False
    try:
        verifiedAccounts.objects.get(user=userObj)
        verification = True
    except:
        verification= False
    if userdata:
        infoObj = info.objects.get(user=userdata.id)
        try:
                    social = socialAcc.objects.get(user=userdata.id)
                    if social:
                        unique_vist_count = ProfileHitsUser.objects.filter(user = userObj.id).count()
                        raw_vist_count = ProfileVisits.objects.filter(user = userObj.id).count()
                        data = {'userdata':[userdata.username,userdata.email],'info':[str(infoObj.dob),str(infoObj.acc_type),infoObj.bio],
                        'social':[social.instagram,social.facebook,social.youtube,social.phone_no,social.twitter,social.snapchat,social.twitch,social.gmail,
                        social.telegram,social.discord],'status':'200','raw_vists_count':raw_vist_count,'unique_vist_count':unique_vist_count,
                        'message':'User found','verification':verification}
                    else:

                        unique_vist_count = ProfileHitsUser.objects.filter(user = userObj.id).count()
                        raw_vist_count = ProfileVisits.objects.filter(user = userObj.id).count()
                        data = {'userdata':[userdata.username,userdata.email],'info':[str(infoObj.dob),str(infoObj.acc_type),infoObj.bio],'status':'204',
                        'message':'User found with no social','raw_vists_count':raw_vist_count,'unique_vist_count':unique_vist_count,'verification':verification}

                    return JsonResponse(data)
        except:
                data = {
                    'userdata':[userdata.username,userdata.email],'info':[str(infoObj.dob),str(infoObj.acc_type),infoObj.bio],'status':'204','vists_count':0,
                    'message':'User found with no social','verification':verification
                }

                return JsonResponse(data)

    else:
            data = {
                'status':'404',
                'message':'Username incorrect hence not found!',
            }

            return JsonResponse(data)


def compPage(request):
    return render(request,'home/compProfile.html')


def compProfile(request):
    if request.method == 'POST':
        dob = request.POST.get('dob')
        ques = request.POST.get('ques')
        ans = request.POST.get('ans')
        bio = request.POST.get('bio')
        infoObj = info.objects.create(bio=bio,user = request.user,dob=dob,security_q = ques,security_ans = ans)
        infoObj.save()
    return redirect('/')


def editProfile(request):
    try:
        if socialAcc.objects.get(user=request.user.id):
            social = socialAcc.objects.get(user=request.user.id)
            context ={
                'socialAccs':social,
            }
            return render(request,'home/profileEdit.html',context)
    except:
        context ={
                'userdata':info.objects.get(user = request.user.id),
            }
        return render(request,'home/profileEdit.html',context)


def editPersonal(request):
    try:
        if info.objects.get(user = request.user.id):
            context ={
                'userdata':info.objects.get(user = request.user.id),
            }
            return render(request,'home/infoEdit.html',context)
    except:
        return redirect('/settings/')


@csrf_exempt
def postInfoAccsUp(request):
    if request.method=='POST':
        insta = request.POST.get('insta')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        youtube = request.POST.get('youtube')
        snapchat = request.POST.get('snapchat')
        twitch = request.POST.get('twitch')
        gmail = request.POST.get('gmail')
        telegram = request.POST.get('tele')
        discordX = request.POST.get('dscord')
        linkedin = request.POST.get('linkedin')
        website = request.POST.get('website')
        phn = request.POST.get('contact')

        if len(phn)==0:
                phn = 0
        if len(gmail) ==0:
                userObj = User.objects.get(username = request.user.username)
                gmail = userObj.email
        try:
            if socialAcc.objects.get(user=request.user.id):
                    userd = socialAcc.objects.get(user=request.user.id)
                    userd.instagram = insta
                    userd.twitter = twitter
                    userd.facebook = facebook
                    userd.youtube = youtube
                    userd.phone_no = phn
                    userd.gmail = gmail
                    userd.telegram= telegram
                    userd.discord = discordX
                    userd.twitch = twitch
                    userd.snapchat = snapchat
                    userd.linkedin = linkedin
                    userd.website = website
                    userd.save()
            else:
                        user_create=socialAcc.objects.create(user = request.user,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,phone_no=phn,gmail=gmail,discord=discordX,linkedin=linkedin,website=website)
                        user_create.save()
        except:
                        user_create=socialAcc.objects.create(user = request.user,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,phone_no=phn,gmail=gmail,discord=discordX,linkedin=linkedin,website=website)
                        user_create.save()
        return HttpResponseRedirect('/')

def updatePersonal(request):
    bio = request.POST.get('bio')
    dob = request.POST.get('dob')
    emoji = request.POST.get('emoji')
    emoji = emoji[0]
    try:
        infoObj = info.objects.get(user = request.user.id)
        infoObj.bio  = bio
        infoObj.dob  = dob
        infoObj.profile_emoji  = emoji
        infoObj.save()
    except User.DoesNotExist:
        return HttpResponse("Server Error!")
    return HttpResponseRedirect("/profile/")

def exProfile(request,username):
    x = returnUserData(request,username)
    return x

def forgotpassword(request):
    return render(request,'home/forgotpass.html')

def generateOTP():
    otp = ''
    i=0
    for i in range(0,4):
        otp+=str(random.randint(0,9))
        i+=1
    if OTPModule.objects.filter(otp=otp,valid=True):
        generateOTP()
    return otp


def requestOtp(request):
    if request.method=="POST":
        email = request.POST.get('email')
        userObj = User.objects.get(email = email)
        ques = request.POST.get('ques')
        ans = request.POST.get('ans')
        infoObjs = info.objects.filter(user = userObj.id,security_q=ques,security_ans = ans)
        if infoObjs:
            return JsonResponse(data={
                'check':'success'
            })
        else:
            return JsonResponse(data={
                'check':'fail'
            })



'''def verifyOtp(request):
    if request.method=="POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        print(email)
        userObj = User.objects.get(email = email)
        otpObj = OTPModule.objects.get(user = userObj.id,otp=otp,valid=True)
        otpObj.valid = False
        otpObj.save()
        if otpObj:
            return HttpResponse('success')
        else:
            return HttpResponse('nope')
    '''

def resetpasswordPage(request):
    return render(request,'home/passreset.html')


def resetPswdDone(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        userObj = User.objects.get(email = email)
        userObj.set_password(password)
        userObj.save()
        return HttpResponse("done")


def automateProcess():
    for i in User.objects.all():
        user = User.objects.get(id = i.id)
        AccountSettings.objects.get_or_create(user = user)

    return "Saved data"

automateProcess()


def usersCount(request):
    automateProcess()
    users = User.objects.all()
    count = users.count()
    data = {
        'count':count,
    }
    return JsonResponse(data)


@csrf_exempt
def putLocationData(request):
    if request.method=="POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        accuracy = request.POST.get('accuracy')
        userObj = User.objects.get(username = request.user.username)
        status = ''
        if latitude and longitude and accuracy:
            try:
                locationObj = locationData.objects.get(user = userObj)

                if locationObj.location_sharing=="on":
                    locationObj.latitude = latitude
                    locationObj.longitude = longitude
                    locationObj.accuracy = accuracy
                    locationObj.save()
            except:
                locationObj = locationData.objects.get_or_create(user = userObj,latitude=latitude,longitude=longitude,accuracy=accuracy)
                locationObj.save()
            status = 'go ahead'
        else:
            status='abort'
    return HttpResponse(status)


@csrf_exempt
def locationSharing(request):
    if request.method=="POST":
        sharing = request.POST.get('sharing')
        userObj = User.objects.get(username = request.user.username)
        status = ''
        try:
            locationObj = locationData.objects.get(user = userObj)
            locationObj.location_sharing = sharing
            locationObj.save()
            status = locationObj.location_sharing
        except:
            status='aborted'
    return HttpResponse(status)


def getLocationSettings(request):
    try:
        userObj = User.objects.get(username = request.user.username)
        locationObj = locationData.objects.get(user = userObj)
        status = locationObj.location_sharing
    except:
        status='aborted'
    return JsonResponse(data={'sharing':status})


@csrf_exempt
def processLoacation(request):
    if request.method=="POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

    userObj = User.objects.get(username = request.user.username)
    R = 6373.0
    def distanceBWlocations(lati1,long1,lati2,long2):
        lat1 = radians(lati1)
        lon1 = radians(long1)
        lat2 = radians(lati2)
        lon2 = radians(long2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c *1000
        return distance
    lati1 = float(latitude)
    long1= float(longitude)
    data_set = locationData.objects.filter(location_sharing='on').exclude(user = userObj.id)
    sorted_lst = []
    for user_data_set in data_set:

        x = distanceBWlocations(lati1,long1,user_data_set.latitude,user_data_set.longitude)
        try:
            userDataLoc = info.objects.get(user = user_data_set.user)
        except:
            pass
        if x<=50:
            sorted_lst.append({'dist':x,'id':userDataLoc.user.username,
                               'userData':{
                                    'bio':userDataLoc.bio,
                                    'user-id':userDataLoc.user.id,
                                    'emoji':userDataLoc.profile_emoji,
                                    'acc_type':userDataLoc.acc_type,
                                    }
                                })
    sorted_data = sorted(sorted_lst , key = lambda i: i['dist'])

    data = {'users':sorted_data}
    return JsonResponse(data)


def updateRegister(request):
    if request.method == "POST":
            email = request.POST.get('email')
            obj = registerData.objects.get_or_create(email = email)
            if obj[1] == True:
                data = {
                        'resp':'created',
                        'status':200
                        }
            else:
                data = {
                        'resp':'exist',
                        'status':401
                        }
            return JsonResponse(data)





@csrf_exempt
def updateMehCard(request):
    if request.method =="POST":
        value = request.POST.get('value')

        acc = AccountSettings.objects.get(user = request.user.id)
        acc.mehCard = value
        acc.save()

        return HttpResponse(acc.mehCard)
    else:
        return HttpResponse("abort")

@csrf_exempt
def updateEventNotification(request):
    if request.method =="POST":
        value = request.POST.get('value')

        acc = AccountSettings.objects.get(user = request.user.id)
        acc.eventNotifications = value
        acc.save()

        return HttpResponse(acc.eventNotifications)
    else:
        return HttpResponse("abort")

@csrf_exempt
def updateInsights(request):
    if request.method =="POST":
        value = request.POST.get('value')

        acc = AccountSettings.objects.get(user = request.user.id)
        acc.insights = value
        acc.save()

        return HttpResponse(acc.insights)
    else:
        return HttpResponse("abort")