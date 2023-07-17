
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self,*args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.category_name


class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name



discount_choices = (
    ("10%","10%"),
    ("20%","20%"),
    ("30%","30%"),
    ("40%","40%"),
    ("50%","50%"),
    ("60%","60%"),
    ("70%","70%"),
    ("80%","80%"),
    ("90%","90%"),
    ("99%","99%"),
)
class Product(models.Model):
    name = models.CharField(max_length=100)
    product_slug = models.SlugField(null=True,blank=True)
    image = models.ImageField(upload_to  = 'upload/')
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name ='products')
    Full_makeup_set = models.BooleanField(default=False,null=True , blank = True)
    new = models.BooleanField(default=False,null = True , blank=True)
    discount = models.BooleanField(default=False,null=True,blank=True)
    percentage = models.CharField(choices=discount_choices,max_length=100, null=True , blank=True ,default='0')
    price = models.IntegerField(null=True,blank=True)
    product_old_price = models.IntegerField(null=True,blank=True)
    product_color = models.ForeignKey(Color,on_delete=models.CASCADE , blank=True,null = True)
    product_discription = models.TextField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.product_slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Slider_image(models.Model):
    heading = models.CharField(max_length=100, null=True,blank=True)
    discription = models.TextField(max_length=100,null=True,blank=True)
    slider_image = models.ImageField(upload_to='upload/slider')
    def __str__(self):
        return self.heading
    

class Information(models.Model):

    email = models.EmailField(null = True , blank=True)
    contact = models.IntegerField(max_length = 11 ,null = True,blank=True)
    address = models.TextField(max_length=100,null=True,blank=True)


class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    

@staticmethod
def prodcut_all():
    return Product.objects.filter(Full_makeup_set = False)


@staticmethod
def prodcut_by_id(cat_id):
    if cat_id:
        return Product.objects.filter(Category = cat_id)
    else:
        return prodcut_all()