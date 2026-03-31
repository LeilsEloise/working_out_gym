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
    }

    return render(request, template, context)
