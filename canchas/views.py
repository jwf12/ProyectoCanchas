from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Sports, Player,  Shift, Reservation, Court
from .forms import ReservationForm, RegistroForm
from .filters import SearchFilter
from datetime import date

from django.utils.decorators import method_decorator


class IndexView(generic.ListView):
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


class CreateReservation2(generic.CreateView, LoginRequiredMixin):
    model = Reservation
    template_name = 'reservation.html'
    context_object_name = 'reservation'
    form_class = ReservationForm
    success_url = reverse_lazy('canchas:index')

    def get_initial(self, **kwargs):
        initial = super(CreateReservation2, self).get_initial(**kwargs)
        shift_id = self.kwargs['shift_id']
        shift = Shift.objects.get(pk=shift_id)
        initial['sport_res'] = shift.court_shift.sport_court.name
        initial['court_res'] = shift.court_shift.name_court
        initial['shift_res'] = shift.hour
        initial['player_res'] = self.request.user
        print('HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa')
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player'] = self.request.user
        shift_id = self.kwargs['shift_id']
        context['shift'] = Shift.objects.get(id=shift_id)
        return context

    def form_valid(self, form):
        shift_id = self.kwargs['shift_id']
        shift = Shift.objects.get(pk=shift_id)

        form.instance.sport_res = shift.court_shift.sport_court
        form.instance.court_res = shift.court_shift
        form.instance.shift_res = shift.hour
        form.instance.player_res = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Reserva creada')
        return response
    
    def form_invalid(self, form):
        shift_id = self.kwargs['shift_id']
        shift = Shift.objects.get(pk=shift_id)
        messages.error(self.request, 'error')
        print(shift.court_shift.sport_court.name)
        print(shift.court_shift.name_court)
        print(shift.hour)
        print(self.request.user)
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
