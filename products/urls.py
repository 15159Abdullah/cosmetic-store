from django.urls import path
from products import views

urlpatterns = [
    path('home/',views.home , name = 'home'),
    path('about/',views.about,  name = 'about'),
    path('contact/',views.contact,name = 'contact'),
    path('shop/',views.shop,name = 'shop'),
    path('detail/<slug:slug>',views.get_detail,name = 'get_detial'),
    path('checkout/',views.checkout,name = 'checkout'),
    path('thankyou/',views.thankyou,name = 'thankyou'),
    path('faq/',views.faq,name = 'faq'),
    path('error/',views.error,name = 'error'),
    path('blog/',views.blog,name = 'blog'),
    path('search_product/',views.search_product,name = 'search_product'),
    path('category_product/<slug:slug>/',views.product_by_cat_slug,name = 'category_product'),
    
]