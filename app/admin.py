from django.contrib import admin
from .models import Product, Address, Cart, BuyOrders

# Register your models here.
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(BuyOrders)