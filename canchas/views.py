from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Sports, Player, Day, Shift, Reservation, Court
from .forms import ReservationForm






class IndexView(generic.ListView):
    model = Day
    template_name = 'index.html'
    context_object_name = 'days'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sports"] = Sports.objects.all()
        context['players'] = Player.objects.all()
        shifts = Shift.objects.all().order_by('hour')
        context['room_name'] = self.kwargs['room_name']
        current_day = self.get_queryset().first() #Aca esta el problema

        filtered_shifts = shifts.filter(day_shift=current_day, status='1')

        context['shifts'] = filtered_shifts 
        context['current_day'] = current_day
        return context



class CreateReservation(generic.DetailView):
    model =Shift
    template_name = 'reservation.html'
    context_object_name ='shift'



class CreateReservation2(generic.CreateView):
    model = Reservation
    template_name = 'reservation.html'
    context_object_name ='reservation'
    form_class = ReservationForm
    success_url = reverse_lazy('canchas:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sports'] = Sports.objects.all()
        context['courts'] = Court.objects.all()
        context['shifts'] = Shift.objects.all().order_by('hour')
        context['players'] = Player.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Reserva creada')
        return response

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)





class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales no validas.')        
        return super().form_invalid(form)
    

class SingUpView(CreateView):
    form_class = UserCreationForm
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
