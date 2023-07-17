
from django.contrib import admin
from acounts.models import *

@admin.register(Order_items)
class Order_itemsAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity','price','paid','status']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','id','phone','email','address','payment','date']
    search_fields = ['name','email']
