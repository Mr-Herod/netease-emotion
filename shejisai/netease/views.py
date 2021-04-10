from django.shortcuts import redirect,render,HttpResponse
from netease import models
import datetime,random
import os

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        url = request.POST.get('url')
        var_song_id = url.split('=')[1]
        os.system('echo \'' + url + '\' | sudo python3 /home/ubuntu/shejisai/static/data_process/comment_spider.py ')
        return render(request,'result.html',locals())


def signin(request):
    if request.method == 'GET':
        return render(request,'sign_in.html')
    else:
        print('Here!!! ')
        username = request.POST.get('username')
        password = request.POST.get('password')
        pwd = models.Users.objects.filter(username = username).values('password')[0]
        print(username,password,pwd)
        if pwd['password'] == password:
            request.session['is_login'] = True      # 登录成功
            request.session.set_expiry(60*60*24*30*12)
            return redirect('index')
        else:
            return redirect('signin')

def signup(request):
    if request.method == 'GET':
        return render(request,'sign_up.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.Users.objects.create(username = username,password = password)
        user_obj.save()
        return redirect('signin')
# Create your views here.
