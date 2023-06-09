from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('listing',views.listing,name='listing'),
    path('display',views.display,name='display'),
    path('like',views.like,name='like'),
    path('wish',views.wish,name='wish'),
    path('cart',views.carts,name='cart'),
    path('mycart',views.mycart,name='mycart'),
    path('logout',views.logout,name='logout'),
    path('mysales',views.mysales,name='mysales'),
    path('remove_cart',views.remove_cart,name='remove_cart'),
    path('like1', views.like1, name = 'like1'),
    path('carts1', views.carts1, name = 'carts1'),
    path('search',views.search,name='search'),
    path('purchase',views.purchase,name='purchase'),
    path('cart_purchase',views.cart_purchase,name='cart_purchase'),
    path('remove_post',views.remove_post,name='remove_post'),
    path('verify',views.verify,name='verify'),
    path('approve',views.approve,name='approve'),
    path('filter/<str:pk>',views.filter,name='filter'),
    path('notapprove',views.notapprove,name='notapprove'),
    path('orders',views.orders,name='orders'),
    path('myorders',views.my_orders,name='myorders'),
    path('forgot_pwd',views.forgot_pwd,name='forgot_pwd'),
    # path('send_otp',views.send_otp,name='send_otp'),
    # path('verify_otp',views.verify_otp,name='verify_otp'),
    path('bidding',views.bidding,name='bidding'),
    path('do_bidding/<str:pk>',views.do_bidding,name='do_bidding'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('sort-by-price/', views.feed_sorted_by_price, name='feed_sorted_by_price'),
    path('sort-by-latest/', views.feed_sorted_by_latest, name='feed_sorted_by_latest'),
    path('report',views.report,name='report'),
    path('report_info',views.report_info,name='report_info'),
    path('notifications',views.bidding_info,name='notifications'),
    path('display1',views.display1,name='display1'),
    path('bid_purchase',views.bid_purchase,name='bid_purchase'),
    path('new_pwd',views.new_pwd,name='new_pwd')
]