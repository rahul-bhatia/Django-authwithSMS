from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import ProfileModel
from random import randrange


# Create your views here.

def usignup(request):
	if request.method=="POST":
		un=request.POST.get('un')
		ph=request.POST.get('ph')
		lo=request.POST.get('lo')
		try:
			usr=User.objects.get(username=un)
			return (request,'usignup',{'msg':'Username already exists'})
		except User.DoesNotExist:
			try:
				usr=ProfileModel.objects.get(phone=ph)
				return (request,'usignup',{'msg':'Phone number already exists'})
			except ProfileModel.DoesNotExist:
				pw=""
				text="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+}{|:"
				for i in range(6):
					pw+=text[randrange(len(text))]
				print("Username : "+un+"\n password:"+pw)
				usr=User.objects.create_user(username=un,password=pw)
				usr.save()
				p=ProfileModel(phone=ph,location=lo,user=usr)
				p.save()
				sms(ph,pw)
				return redirect('ulogin')
	else:
		return render(request,'usignup.html')

def ulogin(request):
	if request.method=="POST":
		un=request.POST.get('un')
		pw=request.POST.get('pw')
		usr=authenticate(username=un,password=pw)
		if usr is None:
			return render(request,'ulogin.html',{'msg':'Bad Credentials'})
		else:
			login(request,usr)
			return redirect('home')
	else:
		return render(request,'ulogin.html')

def ulogout(request):
	logout(request)
	return redirect('ulogin')

def sms(ph,pw):
	import requests
	url = "https://www.fast2sms.com/dev/bulkV2"

	querystring = {"authorization":"Yourfast2smsAPIkey",
	"message":"password:"+str(pw),"language":"english","route":"q","numbers":str(ph)}

	headers = {
    	'cache-control': "no-cache"
    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)


