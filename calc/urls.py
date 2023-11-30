from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name="home"),
    path("calc",views.myCalc,name="myCalc"),
    path("add",views.add,name="add"),
    path("customer",views.create_customer,name='create_customer'),
    path("user",views.create_user,name='create_user'),
    path("customerInfo",views.Customer_view,name='customer_Info'),
]






