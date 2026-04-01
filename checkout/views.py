from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    shoppingbag = request.session.get('bag', {})
    if not shoppingbag:
        messages.error(request, "Your bag is currently empty.")
        return redirect(reverse('merchandise'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
      'order_form': order_form,
      'stripe_public_key': 'pk_test_51THL0p1urpY1vbdfqWYuHsp6HQutigXittGOBRve9PjZ2K7vjPCGSksrJt74ADa1QAdCOIV6SDj2Nx7X0mP5hegD00cn8Pec6c',
      'client_secret': 'test client secret',
    }

    return render(request, template, context)
