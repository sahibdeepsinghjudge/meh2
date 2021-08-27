import usersData
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import OTPModule, info, socialAcc
import pyqrcode
from django.core.mail import BadHeaderError, send_mass_mail
from django.core.mail import EmailMultiAlternatives
from django.template import Context, context
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import png
import random
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, time, timedelta
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
                print("Validation Error")
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
        print(bio,dob,secu_q,ans)
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
        print("ds",discordX)
        if discordX == None:
            discordX = ''
        if telegram == None:
            telegram = ''
        if  gmail or phn:
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

def returnUserData(request,username):
    removeOldOtp()
    try:
        userdata = User.objects.get(username = username)
        if userdata:
            infoObj = info.objects.get(user=userdata.id)
            try:
                social = socialAcc.objects.get(user=userdata.id)
                if social:
                    data = {'userdata':[userdata.username,userdata.email],'info':[str(infoObj.dob),str(infoObj.acc_type),infoObj.bio],'social':[social.instagram,social.facebook,social.youtube,social.phone_no,social.twitter,social.snapchat,social.twitch,social.gmail,social.telegram,social.discord],'status':'200',
                'message':'User found'}
                else:
                    data = {'userdata':[userdata.username,userdata.email],'info':[str(infoObj.dob),str(infoObj.acc_type),infoObj.bio],'status':'204',
                'message':'User found with no social'}
                return JsonResponse(data)
            except:
                data = {
               'userdata':[userdata.username,userdata.email],'info':[str(infoObj.dob),str(infoObj.acc_type),infoObj.bio],'status':'204',
                'message':'User found with no social'
            }
            return JsonResponse(data)
        else:
            data = {
                'status':'404',
                'message':'Username incorrect hence not found!'
            }
            return JsonResponse(data)
    except:
        data = {
                'status':'404',
                'message':'Username incorrect hence not found!'
            }
        return JsonResponse(data)

def editProfile(request):
    try:
        if socialAcc.objects.get(user=request.user.id):
            social = socialAcc.objects.get(user=request.user.id)
            context ={
                'socialAccs':social,
                'userdata':info.objects.get(user = request.user.id),
            }
            return render(request,'home/profileEdit.html',context)
    except:
        context ={
                'userdata':info.objects.get(user = request.user.id),
            }
        return render(request,'home/profileEdit.html',context)

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
        phn = request.POST.get('contact')
        bio = request.POST.get('bio')
        dob = request.POST.get('dob')
        if bio != '':
            userData = info.objects.get(user = request.user.id)
            userData.bio = bio
            userData.save()
        try:
            if socialAcc.objects.get(user=request.user.id):
                    hbd = info.objects.get(user=request.user.id)
                    hbd.dob = dob
                    hbd.save()
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
                    userd.save()
            else:
                    insta = request.POST.get('insta')
                    twitter = request.POST.get('twitter')
                    facebook = request.POST.get('facebook')
                    youtube = request.POST.get('youtube')
                    snapchat = request.POST.get('snapchat')
                    twitch = request.POST.get('twitch')
                    gmail = request.POST.get('gmail')
                    phn = request.POST.get('contact')
                    telegram = request.POST.get('tele')
                    discordX = request.POST.get('dscord')
                    print(insta,facebook,youtube,twitter,snapchat,twitch,gmail,telegram)
                    if  gmail or phn:
                        user_create=socialAcc.objects.create(user = request.user,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,phone_no=phn,gmail=gmail,discord=discordX)
                        user_create.save()
                        print("created with gmail and phn")
                    else:
                        user_create=socialAcc.objects.create(user = request.user,gmail='',phone_no=0,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,discord=discordX)
                        user_create.save()
                        print("created without gmail and phn")
                    hbd = info.objects.get(user=request.user.id)
                    hbd.dob = dob
                    hbd.save()
        except:
                    insta = request.POST.get('insta')
                    twitter = request.POST.get('twitter')
                    facebook = request.POST.get('facebook')
                    youtube = request.POST.get('youtube')
                    snapchat = request.POST.get('snapchat')
                    twitch = request.POST.get('twitch')
                    gmail = request.POST.get('gmail')
                    phn = request.POST.get('contact')
                    telegram = request.POST.get('tele')
                    discordX = request.POST.get('dscord')
                    hbd = info.objects.get(user=request.user.id)
                    hbd.dob = dob
                    hbd.save()
                    print(insta,facebook,youtube,twitter,snapchat,twitch,gmail,telegram)
                    if  gmail or phn:
                        user_create=socialAcc.objects.create(user = request.user,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,phone_no=phn,gmail=gmail,discord=discordX)
                        user_create.save()
                        print("created with gmail and phn")
                    else:
                        user_create=socialAcc.objects.create(user = request.user,gmail='',phone_no=0,instagram=insta,facebook=facebook,telegram=telegram,twitch=twitch,twitter=twitter,youtube=youtube,snapchat=snapchat,discord=discordX)
                        user_create.save()
                        print("created without gmail and phn")
        return HttpResponseRedirect('/')

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
        otp = generateOTP()
        createOTP = OTPModule.objects.create(user = userObj,otp=otp,valid = True)
        print("otp: ",otp)
        createOTP.save()
        to_email = [email]
        subject, from_email, to = 'Meh Password reset email', 'conoughtsservices@gmail.com', to_email
        html_content = render_to_string('otpmail.html',{'user':userObj.username,'otp':otp})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email,bcc=to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return JsonResponse(data={
            'OTP':otp,
            'VALID':'True',
            'EMAIL':'sent',
        })




def verifyOtp(request):
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
    
        
def resetpasswordPage(request):
    return render(request,'home/passreset.html')

def resetPswdDone(request):
    if request.method=='POST':
        email = request.POST.get('email')
        ques = request.POST.get('ques')
        ans = request.POST.get('ans')
        password = request.POST.get('password')
        print(ques,ans)
        userObj = User.objects.get(email = email)
        infoObjs = info.objects.filter(user = userObj.id,security_q=ques,security_ans = ans)
        if infoObjs:
            userObj.set_password(password)
            userObj.save()
            return HttpResponse("done")
        else:
            return HttpResponse("invalids")
