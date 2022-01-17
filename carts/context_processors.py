from .views import _cart_id
from .models import Cart,CartItem
def counter(request):
    cart_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))#select the cart with the cart id equal to the session key
            cart_items=CartItem.objects.all().filter(cart=cart[:1])#select all the cart_items
            for cart_item in cart_items:
                cart_count+=cart_item.quantity

        except Cart.DoesNotExist:
            cart_count=0
    return dict(cart_count=cart_count)
