from django.contrib import admin
from posApp.models import Category, Products, Sales, salesItems, Employees

# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ('code','fullname','contact','status','salary')



admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
admin.site.register(Employees,MyAdmin)
