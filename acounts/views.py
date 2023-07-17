
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from products.models import Product
from acounts.models import Order, Order_items



 
def Login_page(request):
    if request.method =='POST':
        Name = request.POST.get('name')
        Password = request.POST.get('password')
        user = authenticate(username = Name,password = Password)
        request.session['name'] = Name
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Error Name and Password!')
            return HttpResponseRedirect(request.path_info)
           
            
    return render(request,'acounts/login.html')

def Logout_page(request):
    request.session.clear()
    logout(request)
    return redirect('home')    



def Signup_page(request):

    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Re_password = request.POST.get('re_password')
        request.session['name'] = Name
        
        if not Password == Re_password:
            messages.warning(request,'Password Does Not Match!')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.filter(email = Email)
        if user_obj.exists():
            messages.warning(request,'Email Already Exist!')
            return HttpResponseRedirect(request.path_info)

        if  User.objects.filter(username = Name):
            messages.warning(request,'User Name Already Exist!')
            return HttpResponseRedirect(request.path_info)
        
        
        user_obj = User.objects.create(username = Name,email = Email)
        user_obj.set_password(Password)
        user_obj.save()  
        login(request,user_obj)
        return redirect('home')    
    return render(request,'acounts/signup.html')

def Place_order(request):
    if request.method=="POST":
        uid =request.session.get('_auth_user_id')
        user = User.objects.get(id = uid)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address =request.POST.get('address')
        payment = request.POST.get('payment')
        city  = request.POST.get('city')
        post_code = request.POST.get('postcode')
        country = request.POST.get('country')
        description = request.POST.get('description')
        payment_id =request.POST.get('payment_id')
        paid = request.POST.get('paid')
        date = request.POST.get('date')
        
 
        order = Order(
            user = user,
            name = name,
            email = email,
            phone = phone,
            address = address,
            payment = payment,
            city = city,
            post_code = post_code,
            country = country,
            order_description = description,
            payment_id = payment_id,
            date = date     
        )

        order.save()
        cart = request.session.get('cart')
        for i in cart:
            quantity = cart[i]['quantity']
            price = int(cart[i]['price'])
            total = quantity * price
            items = Order_items(
                user = user,
                order = order,
                quantity = cart[i]['quantity'],
                product = cart[i]['name'],
                image = cart[i]['image'],
                price = total,
                paid = paid,
            )
            items.save()
            cart_clear(request)
            
    return render(request,"store/place_order.html")



def Your_order(request):
    uid =request.session.get('_auth_user_id')
    user = User.objects.get(id = uid)

    order = Order_items.objects.filter(user = user)
    context = {'order':order}
    return render(request,'acounts/order.html',context)
 


    #<<<<<<<<<<<<<<......Cart.......>>>>>>>>>>

@login_required(login_url="/acounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/acounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/acounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/acounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    try:
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
    except Exception as e:
        print(e)
    return redirect("cart_detail")


@login_required(login_url="/acounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/acounts/login/")
def cart_detail(request):
    return render(request, 'store/cart.html')



