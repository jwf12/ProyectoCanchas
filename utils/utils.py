from canchas.models import Shift

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings



#change the reservation status to 'reservado'
def reservation_status(pk):
    shift = Shift.objects.get(pk=pk)
    shift.status = 2
    shift.save()


# from django.urls import reverse
# from django.shortcuts import render
# from paypal.standard.forms import PayPalPaymentsForm

# def view_that_asks_for_money(request, shift_id):
#     context={}
#     shift = Shift.objects.get(id=shift_id)

#     # What you want the button to do.
#     paypal_dict = {
#             "business": "sb-fcihl26614756@business.example.com",
#             "amount": int(shift.court_shift.rate / 2),
#             "item_name": f'Cancha: {shift.court_shift.name_court} - Hora: {shift.hour} - Day: {shift.day_shift}',
#             "invoice": shift.id,
#             "return_url": request.build_absolute_uri(reverse('canchas:reservation2', kwargs={'shift_id': shift.id})),
#         }

#     # Create the instance.
#     paypal = PayPalPaymentsForm(initial=paypal_dict)
#     context['paypal'] = paypal
#     return render(request, "reservation.html", context)
