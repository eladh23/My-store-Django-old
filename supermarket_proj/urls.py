from django.urls import path
from . import views

urlpatterns = [
    path('product', views.products, name="products"), 
    path('product/<id>', views.product_detail, name="product_detail"),  
    
]