from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem

def cart(request):
    session_id = request.session.session_key
    cartid = Cart.objects.get(cart_id = session_id)
    cart_id=Cart.objects.filter(cart_id = session_id).exists()
    
    cart_items = None
    tax =0
    total = 0
    grand_total =0
    if cart_id:
        cart_items = CartItem.objects.filter(cart = cartid)
        for item in cart_items:
            total += item.product.price * item.quantity
    
    tax = (2*total)/100
    grand_total = tax + total
    
    return render(request, 'cart/cart.html', {'cart_items':cart_items, 'tax':tax, 'total':total, 'grand_total':grand_total})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    session_id = request.session.session_key
    cart_id = Cart.objects.filter(cart_id = session_id).exists()
    if cart_id:
        cart_item = CartItem.objects.filter(product=product).exists()
        if cart_item:
            item = CartItem.objects.get(product=product)
            item.quantity += 1
            item.save()
        else :
            cartid = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
                cart = cartid,
                product = product,
                quantity = 1
            )
            item.save()
    else:
        cart = Cart.objects.create(
        cart_id = session_id
        )
        cart.save()
    
    return redirect('cart')
    
    

def remove_cart_item(request, product_id):
    print(product_id)
    product = Product.objects.get(id = product_id)
    session_id = request.session.session_key
    cartid = Cart.objects.get(cart_id = session_id) # cart search korlam
    cart_item = CartItem.objects.get(cart =cartid, product=product) # cart item filter korbo cartid ar product id er upor filter korbo
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    print(type(cart_item))
    return redirect('cart')

def delete_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    session_id = request.session.session_key
    cartid = Cart.objects.get(cart_id = session_id) # cart search korlam
    cart_item = CartItem.objects.get(cart =cartid, product=product) # cart item filter korbo cartid ar product id er upor filter korbo
    cart_item.delete()
    return redirect('cart')