from django.shortcuts import render
from store.models import Product
from . models import Cart,CartItem
from . cart import _cart_id
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.
def cart(request,total=0,quantity=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (3* total)/100
        grand_total = total + tax
    except Cart.ObjectNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total
    }

    return render(request,'cart/cart-summary.html',context)

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id) #To get product ID
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) #To get cart ID

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )

    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity +=1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity =1,
            cart = cart,
        )
        cart_item.save()

    return redirect('cart')


def remove_cart(request, product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product, id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity>1:
        cart_item.quantity -=1
        cart_item.save()

    else:
        cart_item.delete()

    return redirect('cart')

def remove_cart_item(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product, id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart')

def checkout(request):
    return render(request,'cart/checkout.html')


