
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
 
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderd = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)


class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    payment = models.TextField()
    city  = models.CharField(max_length=50)
    post_code = models.TextField(null = True, blank=True)
    country = models.CharField(max_length=50)
    order_description = models.CharField(max_length=200,blank=True, null=True)
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateTimeField(auto_now_add =True, null=True)

    def __str__(self):
        return self.user.username

class Order_items(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload/order_product')
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.BooleanField(default=False,null=True)
    paid = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.order.user.username
