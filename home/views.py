from usersData.models import info, socialAcc
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request,'home/main.html')

def search(request):
    return render(request,'home/searchPage.html')

def basicSearch(request):
    if request.method=="POST":
        query = request.POST.get('query')
        if query == "":
            return JsonResponse(data={"objs":""})
        else:
            obj_res = User.objects.filter(username__contains=query)| \
                User.objects.filter(email__contains=query)
            obj_social = socialAcc.objects.filter(instagram__contains=query)| \
                socialAcc.objects.filter(snapchat__contains=query)| \
                socialAcc.objects.filter(twitter__contains=query)| \
                socialAcc.objects.filter(twitch__contains=query)| \
                socialAcc.objects.filter(gmail__contains=query)| \
                socialAcc.objects.filter(facebook__contains=query)
            data = {
                'objs':[],'social':[]
            }
            for i in obj_res:
                data['objs'].append(i.username)
            for i in obj_social:
                data['social'].append(i.user.username)
            return JsonResponse(data)

def exProfilePage(request,username):
    context = {
        'user_to':username
    }
    return render(request,'home/exProfile.html',context)


def loginPage(request):
    logout(request)
    return render(request,'home/login.html')

def registerPage(request):
    logout(request)
    return render(request,'home/registerOne.html')

def launchSettings(request):
    if request.user.is_authenticated:
        userObj = User.objects.get(username = request.user)
        infoObj = info.objects.get(user = userObj)
        context = {
            'data':infoObj
        }
        return render(request,'home/settings.html',context)
    else:
        return redirect("/")

def myProfile(request):
    return render(request,'home/myProfile.html')

