import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from shop.models import product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from shop.serializers import UserCartSerializer
from shop.models import User_cart
from rest_framework import viewsets



# Create your views here.
def home_page(request):
    top_wear=product.objects.filter(product_category='t')
    foot_wear=product.objects.filter(product_category='f')
    all_product={
        'topwear':top_wear,
        'topwear_len':len(top_wear),
        'footwear':foot_wear,
        'footwear_len':len(foot_wear),
        }
    return render(request,'shop/home.html',all_product)

def product_detail(request,id):
    product_detail=product.objects.get(pk=id)
    discount=product_detail.product_discount
    price=product_detail.product_price
    discounted_price=price-price*discount/100
    return render(request,'shop/product.html',{'product':product_detail,'discounted_price':discounted_price})


def user_cart(request):
    return render(request,'shop/cart.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        check_val=request.POST.get('check',False)
        if check_val=='on':
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'You have successfully Login')
                return redirect('/')
            else:
                return redirect('/')
        else:
            return redirect('/')

def user_logout(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            logout(request)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

class update_cart(viewsets.ModelViewSet):
    queryset=User_cart.objects.all()
    serializer_class=UserCartSerializer







