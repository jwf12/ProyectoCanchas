from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import IndexView, CustomLoginView, SingUpView, CreateReservation2



app_name = 'canchas'

urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), {'room_name': 'padel'}, name='index'),
    path('tenis/', IndexView.as_view(template_name='tenis.html'), {'room_name': 'tenis'}, name='tenis'),
    path('createreservation/<int:shift_id>/', CreateReservation2.as_view(), name='reservation2'),
    path('createreservation2/<int:shift_id>/', CreateReservation2.as_view(template_name='reservation2.html'), name='reservation3'),
    

    path('login/', CustomLoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('register/', SingUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'login.html'), name='logout'),


    path('paypal/', include("paypal.standard.ipn.urls")),
]
