from django.urls import path
from app import views
urlpatterns = [
    path('', views.home),
    path('product/<int:id>', views.product_detail, name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('explore/', views.explore, name='explore'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-placed/', views.orderplaced, name='orderplaced'),
]