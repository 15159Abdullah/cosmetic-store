from django.urls import path
from acounts import views

urlpatterns = [
    path('login/',views.Login_page,name = 'login'),
    path('signup/',views.Signup_page,name = 'signup'),
    path('logout/',views.Logout_page,name = 'logout'),
    path('place_order/',views.Place_order,name = 'place_order'),
    path('your_order/',views.Your_order,name = 'your_order'),

    #cart>>>>>>>>

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'), 
]