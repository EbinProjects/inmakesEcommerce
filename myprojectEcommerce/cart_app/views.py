from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from myapp.models import Product
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def cardID(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def addToCart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_ID=cardID(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_ID=cardID(request))
        cart.save()
    try:
        cartItem = CartItem.objects.get(product=product, cart=cart)
        if cartItem.quantity < cartItem.product.stock:
            cartItem.quantity += 1
        cartItem.save()
    except CartItem.DoesNotExist:
        cartItem = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cartItem.save()

    return redirect('cart_app:cart_Details')


def cart_Details(request, total=0, counter=0, cart_item=None):
    try:
        cart = Cart.objects.get(cart_ID=cardID(request))
        cart_item = CartItem.objects.filter(cart=cart, active=True)
        for cart_iem in cart_item:
            total += (cart_iem.product.price * cart_iem.quantity)
            counter += cart_iem.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cartitem=cart_item, total=total, counter=counter))


def minusCart(request, product_id):
    cart = Cart.objects.get(cart_ID=cardID(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_app:cart_Details')


def removeCart(request, product_id):
    cart = Cart.objects.get(cart_ID=cardID(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_Details')
