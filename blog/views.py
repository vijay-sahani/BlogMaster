from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse

def check_auth(request):
    if request.user.is_authenticated :
        if request.user.is_staff and request.user.is_superuser:
            return redirect('admin:index')
    return render(request,'404.html')



def handleSignup(request):
    if request.method=='POST':
        # Getting the creadtials
        fname=request.POST['fname']
        lname=request.POST['lname']
        user_name=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1!=pass2:
            messages.error(request, '<strong>Password\'s doesn\'t match!</strong>')
            return redirect('index')
        try:
            myuser=User.objects.create_user(user_name,email,pass1)
        except Exception as e:
            messages.error(request,'<strong>Username Already exist!</strong> Please enter different username')
            return redirect('index')
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, '<strong>Congratulation!</strong> Your account has been created.')
        return redirect('index')
    return render(request,'404.html')



def handleLogin(request):
    if request.method=='POST':
        loginUser=request.POST['loginUsername']
        loginPassword=request.POST['loginPass']
        user=authenticate(request,username=loginUser,password=loginPassword)
        if user is not None:
            messages.success(request,f'Welcome back <strong>{loginUser}</strong>')
            login(request,user)
        else:
            messages.error(request,'<strong>Invalid creadtials!</strong> Please enter correct details.')
        return redirect('index')
    return render(request,'404.html')

    

def handleLogout(request):
    if request.user.username:
        logout(request)
        return redirect('index')
    return render(request,'404.html')