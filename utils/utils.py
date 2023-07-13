from canchas.models import Shift

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm



#change the reservation status to 'reservado'
def reservation_status(pk):
    shift = Shift.objects.get(pk=pk)
    shift.status = 2
    shift.save()

def view_that_asks_for_money(request):
    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    paypal = PayPalPaymentsForm(initial=paypal_dict)
    context = {"paypal": paypal}
    return render(request, "pay.html", context)
