import imp
from django.contrib import admin
from django.forms import models
from shop.models import product,User_cart

# Register your models here.
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','product_brand','product_category','product_price','product_image','product_description','rating','product_discount']

@admin.register(User_cart)
class UserCartAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']