from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        upassword = request.POST.get('password')

        user = authenticate(request,username=uname,password=upassword)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username Don't exist / Password is incorrect ")
        
    return render(request,'login.html')

def signup_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        uemail = request.POST.get('email')
        upassword1 = request.POST.get('password1')
        upassword2 = request.POST.get('password2')

        if upassword1 != upassword2:
            return HttpResponse("Possword do not match!!")
        
        try:
            #error occur if data is not in database that's why we create expections handling..
            name = User.objects.get(username=uname) 
            return HttpResponse('Username is already registered')
        except User.DoesNotExist:
            my_user = User.objects.create_user(uname, uemail, upassword1)
            my_user.save()
            return redirect('login')
           
        
    return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='home')
def home(request):
    current_user = request.user
    context ={}
    context['username']=current_user.username
    context['email'] = current_user.email
    context['id'] = current_user.id
    return render(request,'index.html',context)

def delete_view(request):
    user = request.user
    user.delete()
    logout(request)
    return redirect('login')