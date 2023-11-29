from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.

def home(request):
    return render(request, 'home.html',{"name":"Prabhakar"})


def myCalc(request):
    return render(request,'calc2.html',{"name":"Siva"})