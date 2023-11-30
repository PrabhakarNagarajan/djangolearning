from django import forms
from .models import Customer,User



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email', 'incharge_name', 'incharge_email', 'GSTIN']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','descri']