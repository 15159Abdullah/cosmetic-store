
from django.conf import settings
from django.shortcuts import redirect, render
from products.models import *
from django.core.mail import send_mail

def home(request):
    
    data = Product.objects.filter(new = True)
    data2 = Product.objects.filter(discount = True)
    data3 = Product.objects.filter(Full_makeup_set = True)
    context = {'new':data,'discount':data2,'makeup_set':data3}
    return render(request,'store/index.html',context)

def about(request):
    return render(request,'store/about.html')

def blog(request):
    return render(request,'store/blog.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_to = [email]
        email_from = settings.EMAIL_HOST_USER
        subject = subject
        message = f'Hi my name is {name}.' + message
        send_mail(subject,message,email_from,email_to)

        contact = Contact_us(
            name = name,
            phone = phone,
            email = email,
            subject = subject,
            message = message

        )
        contact.save()
        
    return render(request,'store/contact.html')

def checkout(request):
    return render(request,'store/checkout.html')

def shop(request):
    obj_shop = prodcut_all()
    obj_cat = Category.objects.all()
    data = {'products':obj_shop,'category':obj_cat}

    return render(request,'store/shop.html',data)

def product_by_cat_slug(request,slug):
    obj_cat = Category.objects.all()
    cat_slug = Category.objects.get(category_slug=slug)

    product_by_slug = Product.objects.filter(product_category = cat_slug)
    context = {'cat':cat_slug,'product':product_by_slug,'category':obj_cat}

    return render(request,'store/category_product.html',context)
 
def thankyou(request):
    return render(request,'store/thankyou.html')

def faq(request):
   
    return render(request,'store/faq.html')

def get_detail(request,slug):
    prod = Product.objects.filter(product_slug=slug)

    if prod.exists():
        prod=Product.objects.get(product_slug=slug)
    else:
        return redirect('error')
    context = {'prod':prod}
    
    return render(request,'store/detail.html',context)


def error(request):
    return render(request,'store/404.html')


def search_product(request):
    query = request.GET.get('q')
    data = Product.objects.filter(name__icontains = query)
    cat = Category.objects.all()
    contex = {'data':data,'category':cat}
    return render(request,'store/search_product.html',contex)
