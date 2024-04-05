from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Customer
from django.contrib import messages
# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('home')
def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            # USER ACCOUNT CREATION
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            # customer account creation
            customer = Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            success_massage = "user registration successful"
            messages.success(request,success_massage)

        except Exception as e:
            error_message = "Duplicate username or invalid inputs"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user :
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'invalid user credentials')


    return render(request,'account.html',context)