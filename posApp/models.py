from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.

class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    fullname = models.CharField(max_length=100) 
    gender = models.CharField(max_length=100,blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.CharField(max_length=100) 
    address = models.CharField(max_length=100) 
    email = models.CharField(max_length=100)  
    date_hired = models.DateField(auto_now=True) 
    salary = models.FloatField(default=0) 
    status = models.CharField(max_length=100) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.firstname) + ' ' +str(self.middlename )+ ' '+str(self.lastname) + ' '
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Products(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code + " - " + self.name

class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)