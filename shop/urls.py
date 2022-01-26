import imp
from . import views
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('add',views.update_cart,basename='cart')

urlpatterns = [
    path('',views.home_page,name='home'),
    path('product/<int:id>',views.product_detail,name='product_detail'),
    path('cart/',views.user_cart,name='cart'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('',include(router.urls)),
]
