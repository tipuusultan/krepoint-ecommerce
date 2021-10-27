from django.db import models
from django.shortcuts import redirect, render
from .models import BuyOrders, Cart, Product, Address, BuyOrders
from django.contrib import messages

delivery_charge = 70

def home(request):
    try:
        cart = Cart.objects.filter(user=request.user)
        address = Address.objects.filter(user=request.user)
        products = Product.objects.filter(status=True)
        context = {'products':products, 'address':address, 'cart_quantity':len(cart)}
        return render(request, 'app/home.html', context)
    except: 
        products = Product.objects.filter(status=True)
        context = {'products':products}
        return render(request, 'app/home.html' , context)


def explore(request):
    products = Product.objects.all()
    try:
        cart = Cart.objects.filter(user=request.user)
        context = {'products':products, 'cart_quantity':len(cart)}
        return render(request, 'app/explore.html', context)
    except TypeError:
        context = {'products':products}
        return render(request, 'app/explore.html', context)

def product_detail(request, id):
    if request.method == 'POST':
        product_ob = Product.objects.filter(id=id)
        product_title = product_ob[0].title
        cart_product_exist = Cart.objects.filter(user=request.user ,product=product_ob[0])
        if cart_product_exist.exists():
            product_quantity = cart_product_exist[0].quantity
            cart_product_exist.update(quantity=product_quantity+1)
            messages.success(request, "Cart Updated.")
        else:
            item = Cart(user=request.user, product=product_ob[0])
            item.save()
            messages.success(request, "Product Added to your Cart")
        

    cart = Cart.objects.filter(user=request.user)
    product = Product.objects.filter(id=id)
    context = {'product':product, 'cart_quantity':len(cart)}
    return render(request, 'app/productdetail.html',context)

def cart(request):
    cart = Cart.objects.filter(user=request.user)

    # checkiing total cart value 
    total_cart_value = 0
    for c in cart:
        total_cart_value = total_cart_value + c.product.price
    context = {'cart_quantity':len(cart) ,
                'items':cart,
                'total_cart_value':total_cart_value+delivery_charge,
                'cart_value':total_cart_value,
                'delivery_charge':delivery_charge}
    return render(request, 'app/addtocart.html', context)



def buy_now(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart_quantity':len(cart)}
    return render(request, 'app/buynow.html', context)

def profile(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart_quantity':len(cart)}
    return render(request, 'app/profile.html', context)

def address(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart_quantity':len(cart)}
    return render(request, 'app/address.html', context)

def orders(request):
    buyorders = BuyOrders.objects.filter(user=request.user)
    cart = Cart.objects.filter(user=request.user)
    context = {
        'cart_quantity':len(cart),
        'orders':buyorders,
        }
    return render(request, 'app/orders.html', context)

def change_password(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart_quantity':len(cart)}
    return render(request, 'app/changepassword.html', context)

def mobile(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart_quantity':len(cart)}
    return render(request, 'app/mobile.html', context)

def checkout(request):
    if request.method =='POST':
        address = Address.objects.filter(user=request.user)

        # checking the address is already added or not 
        if not address:
            address_exist = False
        else:
            address_exist = True

        cart_id = request.POST.get('cartid')
        total_cart_item = Cart.objects.filter(id=cart_id ,user=request.user)
        cart = Cart.objects.filter(id=cart_id ,user=request.user)
        cart_total_price = 0
        for c in cart:
            cart_total_price = (cart_total_price+c.product.price)*c.quantity+delivery_charge
            print(cart_total_price)

        paymentmethods = ['Cash on Delivery' , 'Debit/Credit Card' , 'UPI/Wallet']
        context = {
            'cart_quantity':len(total_cart_item),
            'cart':cart,
            'address':address,
            'address_exist':address_exist,
            'cart_total_price':cart_total_price,
            'paymentmethods':paymentmethods,
        }

        return render(request, 'app/checkout.html', context)
    else:
        return redirect('/')

def orderplaced(request):
    if request.method == 'POST':
        cartid = request.POST.get('cartid')
        addressid = request.POST.get('address')
        PaymentMethod = request.POST.get('paymentmethod')

        cart = Cart.objects.filter(id=cartid)
        address = Address.objects.filter(id=addressid)
        order = BuyOrders(user=request.user , cart=cart[0], address=address[0], paymentMethod=PaymentMethod)
        order.save()
        return render(request, 'app/order_placed.html')
    
    else:
        return redirect('/')