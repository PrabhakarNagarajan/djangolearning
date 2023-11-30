from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from  .models import User
from .models import Customer
from .forms import CustomerForm,UserForm
# Create your views here.

def home(request):
    return render(request, 'home.html',{"name":"Prabhakar"})


def myCalc(request):

    dests = User.objects.all()
    return render(request,'calc2.html',{"dest":dests})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request,"result.html",{"Result":res})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    else:
        form = CustomerForm()
    return render(request,'create_customer.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('/user')
    else:
        userForm = UserForm()
    return render(request,'create_user.html',{'userform':userForm})



def Customer_view(request):
    userData = Customer.objects.all()
    return render(request,"user_info.html",{"userdata":userData})