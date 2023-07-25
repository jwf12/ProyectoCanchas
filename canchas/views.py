from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import generic

from utils.utils import reservation_status
from .models import Sports, Player,  Shift, Reservation, Court
from .forms import ReservationForm, RegistroForm
from .filters import SearchFilter
from datetime import date
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Shift
    context_object_name = 'shifts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sports"] = Sports.objects.all()
        context['players'] = Player.objects.all()
        context['room_name'] = self.kwargs['room_name']
        context['today'] = date.today()

        # Llamar a searchView y pasar el resultado
        search_result = self.searchView(self.request)
        context.update(search_result)

        return context

    #Funcion para el filtro de fecha, usa el decorador para que no tenga acceso a los atributos e instancias de la clase
    @staticmethod
    def searchView(request):
        shift = Shift.objects.all().order_by('hour')    
        myFilter = SearchFilter(request.GET, queryset=shift)
        shifts = myFilter.qs
        
        return {
            'myFilter': myFilter,
            'shifts': shifts,
        }


class CreateReservation2(LoginRequiredMixin, generic.CreateView):
    model = Reservation
    template_name = 'reservation.html'
    context_object_name = 'reservation'
    form_class = ReservationForm
    success_url = reverse_lazy('canchas:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player'] = self.request.user
        shift_id = self.kwargs['shift_id']
        shift = Shift.objects.get(id=shift_id)
        context['shift'] = shift
        paypal_dict = {
            "business": "sb-fcihl26614756@business.example.com",
            "amount": shift.court_shift.rate / 2,
            "item_name": f'Cancha: {shift.court_shift.name_court} - Hora: {shift.hour} - Day: {shift.day_shift}',
            "invoice": shift.id,
            "return": self.request.build_absolute_uri(reverse('canchas:reservation3', kwargs={'shift_id': shift.id})),
        }

        # Create the instance.
        paypal = PayPalPaymentsForm(initial=paypal_dict)
        context['paypal'] = paypal
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        shift_id = self.kwargs['shift_id']
        shift = Shift.objects.get(pk=shift_id)
        kwargs['initial'] = {
            'sport_res': shift.court_shift.sport_court,
            'court_res': shift.court_shift,
            'shift_res': shift,
            'rate_res': shift.court_shift.rate,
            'player_res': self.request.user,
        }
        return kwargs
    
    def send_reservation_email(self):
        shift_id = self.kwargs['shift_id']
        shift = Shift.objects.get(pk=shift_id)
        mail = self.request.user.email
        sport_res = shift.court_shift.sport_court
        court_res = shift.court_shift
        shift_res = shift
        rate_res = shift.court_shift.rate
        player_res = self.request.user
        day_shift = shift.day_shift
        subject = f'Reserva cancha de {shift.court_shift.sport_court}'

        print(mail)

        html_content = render_to_string('email.html', {
        'sport_res': sport_res,
        'court_res': court_res,
        'shift_res': shift_res,
        'rate_res': rate_res,
        'player_res': player_res,
        'day_shift': day_shift,
        'saldo': shift.court_shift.rate / 2
    })
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=['julianwf12@gmail.com', mail]
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
    
    def form_valid(self, form):
        #change the reservation status to 'reservado', function in utils  ---- 
        shift_id = self.kwargs['shift_id']
        reservation_status(shift_id)
        
        # sends an email when the reservation its completed to the owner of the court
        self.send_reservation_email()

        response = super().form_valid(form)
        messages.success(self.request, 'Reserva creada')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'error')
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales no validas.')        
        return super().form_invalid(form)
    

class SingUpView(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('canchas:login')
    template_name = 'register.html'

    def form_valid(self, form):        
        response = super().form_valid(form)
        messages.success(self.request, '¡Tu cuenta ha sido creada! Por favor inicia sesión.')
        return response
            
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Las contraseñas no coinciden.')        
        return response
    
