from .models import Reservation
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields=[
        'sport_res',
        'court_res',
        'shift_res',
        'player_res',
    ]
        