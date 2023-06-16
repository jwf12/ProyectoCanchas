from django.contrib import admin
from .models import Player, Sports, Court, Day, Shift, Reservation, Payment
# Register your models here.



class SportAdmin(admin.ModelAdmin):
    list_display=(
        'name',
    )


class CourtAdmin(admin.ModelAdmin):
    list_display=(
        'sport_court',
        'name_court',
        'rate',
        'court_type'
    )
    list_filter=(
        'sport_court',
        'name_court',
        'court_type')
    search_fields=(
        'sport_court',
        'name_court',
        'court_type')
    

class DayAdmin(admin.ModelAdmin):
    list_display=('day',)
    list_filter=('day',)
    search_fields=('day',)


class ShiftAdmin(admin.ModelAdmin):
    list_display=(
        'court_shift',
        'day_shift',
        'hour',
        'status'
    )
    list_filter=(
        'hour',
        'status'
    )
    search_fields=(
        'hour',
        'status'
    )


class ReservationAdmin(admin.ModelAdmin):
    list_display=(
        'sport_res',
        'court_res',
        'shift_res',
        'player_res',

    )
    list_filter=('sport_res', 'court_res', 'player_res')
    search_fields=('sport_res', 'player_res',)
    

class PaymentAdmin(admin.ModelAdmin):
    list_display=('reservation_pay', 'method')
    list_filter=('reservation_pay', 'method')
    search_fields=('reservation_pay', 'method')
    


admin.site.register(Player)
admin.site.register(Sports, SportAdmin)
admin.site.register(Court, CourtAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Payment, PaymentAdmin)