from django.urls import path
from . import views

urlpatterns = [
    path('',views.web1,  name='home'),
    path('product2/',views.web2,  name='product2'),
    path('signup/',views.web11,  name='signup'),
    path('signup/register',views.web11,  name='sign up'),
    path('login/',views.loginpage,  name='login'),
    path('logout/',views.web13,  name='logout'),
    path('signup/login/',views.loginpage,  name='login'),
    path('single2/',views.web3,  name='single2'),
    path('checkout/',views.web4,  name='checkout'),
    path('product/checkout/',views.web4,  name='checkout'),
    path('product2/checkout/',views.web4,  name='checkout'),
    path('single/checkout/',views.web4,  name='checkout'),
    path('single2/checkout/',views.web4,  name='checkout'),
    path('help/',views.web5,  name='help'),
    path('payment/',views.web6,  name='payment'),
    path('product/',views.web7,  name='product'),
    path('single/',views.web8,  name='single'),
    path('terms/',views.web9,  name='terms'),
    path('contact/',views.web10,  name='contact'),
    
   
]
