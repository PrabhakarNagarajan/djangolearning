from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.

def home(request):
    return render(request, 'home.html',{"name":"Prabhakar"})


def myCalc(request):
    return render(request,'calc2.html',{"name":"Siva"})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request,"result.html",{"Result":res})