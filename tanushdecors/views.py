# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render
from django.views import generic
from django.utils import timezone
from .models import CartItem, Product

class IndexView(generic.ListView):
    """
    IndexView: Displays the latest products.
    """
    template_name = 'tanushdecors/index.html'
    context_object_name = 'latest_product_list'

    def get_queryset(self):
        """
        Fetches the latest 5 products published before or at the current time, ordered by publication date.
        """
        return Product.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def product_list(request):
    products = Product.objects.all()
    return render(request, 'tanushdecors/products.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'tanushdecors/shop.html', {'products': products})

def about(request):
    return render(request, 'tanushdecors/about.html')

def services(request):
    return render(request, 'tanushdecors/services.html')

def blog(request):
    return render(request, 'tanushdecors/blog.html')

def contact(request):
    return render(request, 'tanushdecors/contact.html')



def thankyou(request):
    return render(request, 'tanushdecors/thankyou.html')

def login(request):
    return render(request, 'tanushdecors/login.html')

def checkout(request):
    return render(request, 'tanushdecors/checkout.html')


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'tanushdecors/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('tanushdecors:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()

    return redirect('tanushdecors:view_cart')

