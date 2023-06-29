from canchas.models import Shift

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


#change the reservation status to 'reservado'
def reservation_status(pk):
    shift = Shift.objects.get(pk=pk)
    shift.status = 2
    shift.save()


def email(request):
    if request.method == 'POST':
        sport_res = request.POST['sport_res']
        court_res = request.POST['court_res']
        shift_res = request.POST['shift_res']
        rate_res = request.POST['rate_res']
        player_res = request.POST['player_res']

    template = render_to_string('email.html'), {
        'sport_res': sport_res,
        'court_res': court_res,
        'shift_res': shift_res,
        'rate_res': rate_res,
        'player_res': player_res,

    }