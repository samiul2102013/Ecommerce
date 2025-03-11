from django.shortcuts import render

def Cart(request):
    return render(request, 'cart/cart.html')