from rest_framework import serializers
from shop.models import User_cart

class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_cart
        fields=['user','product','quantity']