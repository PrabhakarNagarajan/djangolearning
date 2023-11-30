from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    descri = models.TextField(default="Default description")
    img= models.ImageField(upload_to='pics')


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=200)
    incharge_name = models.CharField(max_length=100)
    incharge_email = models.EmailField(max_length=200)
    GSTIN = models.CharField(max_length=100)
    customer_relationship_start_date= models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
