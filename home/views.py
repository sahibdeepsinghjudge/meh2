from usersData.models import socialAcc
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'home/main.html')

def search(request):
    return render(request,'home/searchPage.html')

def basicSearch(request):
    if request.method=="POST":
        query = request.POST.get('query')
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