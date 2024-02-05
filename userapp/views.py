from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if username == '' or email == '' or password == '':
            messages.warning(request,'Error Empty')
            return redirect('/register')
        
        else:
            if User.objects.filter(username=username):
                messages.warning(request,'Error Empty')
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('/login')
            
    return render(request,'register.html')




def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if username == '' or password == '':
            messages.warning(request,'โปรดกรอกID-PASSWORD ให้ถูกต้อง')
            return redirect('/login')
        elif user is None:
            messages.warning(request,'ไม่พบIDนี้อยู่ในระบบ')
            return redirect('/login')
        
        else:
            if user is not None:
                auth.login(request,user)
                return redirect('/')
         
    return render(request,'login.html')





def logout(request):
    auth.logout(request)
    return redirect('/login') 
    
