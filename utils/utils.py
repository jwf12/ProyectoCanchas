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

