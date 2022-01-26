from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class product(models.Model):
    product_image=models.ImageField()
    product_name=models.CharField(max_length=500)
    product_brand=models.CharField(max_length=150,default='')
    product_price=models.IntegerField()
    product_category=models.CharField(max_length=1, choices=[('t',"Top Wear"),('b','Bottom Wear'),('f','Foot Wear')])
    product_description=models.CharField(max_length=500)
    product_discount=models.IntegerField()
    rating=models.FloatField()


class User_cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField()



