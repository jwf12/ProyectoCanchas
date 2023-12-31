from .models import Reservation, Player
from django import forms
from django.contrib.auth.forms import UserCreationForm


#Form para creacion de reserva
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'sport_res',
            'court_res',
            'shift_res',
            'rate_res',
            'player_res',
        ]



#Creacion de usuario
class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label='Name', required=True)
    last_name = forms.CharField(label='Last-name', required=True)
    age = forms.CharField(label='age')
    SEX_OPTION = (
        ('1','Female'),
        ('2', 'Male')
    )
    email = forms.EmailField(required=True)
    sex = forms.TypedChoiceField(label='Sex', choices=SEX_OPTION, coerce=str)
    password1 = forms.CharField(label='password',widget = forms.PasswordInput, required=True)
    password2 = forms.CharField(label='confirm-password',widget = forms.PasswordInput, required=True)


    class Meta:
        model = Player
        fields = [
            'username',            
            'first_name',
            'last_name',
            'age',
            'email',
            'sex',
            'password1',
            'password2',        
        ]