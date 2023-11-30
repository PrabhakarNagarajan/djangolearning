from django.urls import path
from . import views
from .views import create_customer


urlpatterns =[
    path('',views.home,name="home"),
    path("calc",views.myCalc,name="myCalc"),
    path("add",views.add,name="add"),
    path("customer",create_customer,name='create_customer')
]






