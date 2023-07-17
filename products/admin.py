
from django.contrib import admin

from products.models import *

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model=Product

    list_display = ['name','id','price','product_color','Full_makeup_set','discount','new','percentage']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    model = Color
    list_display =['color_name']


@admin.register(Contact_us)
class Contact_usAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','subject','message']

@admin.register(Slider_image)
class ColorAdmin(admin.ModelAdmin):
    model = Slider_image
    list_display =['heading','slider_image','discription']



@admin.register(Information)
class ColorAdmin(admin.ModelAdmin):
    model = Information
    list_display =['email','contact','address']



