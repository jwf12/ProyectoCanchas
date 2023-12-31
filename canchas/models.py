from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField


class Player(AbstractUser):
    pass


class Sports(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Court(models.Model):
    sport_court = models.ForeignKey(Sports, on_delete=models.CASCADE)
    name_court = models.CharField(max_length=50)
    rate = models.IntegerField()
    COURT_TYPE_TUPLE=(
        ('1', 'Cemento'),
        ('2', 'Sintetico'),
        ('3', 'Parquet')

    )
    court_type = models.CharField(max_length=50,choices=COURT_TYPE_TUPLE)

    def __str__(self):
        return self.name_court


class Shift(models.Model):
    court_shift = models.ForeignKey(Court, on_delete=models.CASCADE)
    day_shift = models.DateField()
    hour = models.CharField(max_length=5)
    STATUS_SHIFT=(
            ('1', 'Disponible'),
            ('2', 'Reservado'),
        )
    status = models.CharField(max_length=50,choices=STATUS_SHIFT, default=1)

    def __str__(self):
        return self.hour


class Reservation(models.Model):
    sport_res = models.ForeignKey(Sports, on_delete=models.CASCADE)
    court_res = models.ForeignKey(Court, on_delete=models.CASCADE)
    shift_res = models.ForeignKey(Shift, on_delete=models.CASCADE)
    rate_res = models.IntegerField()
    player_res = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.rate_res = self.court_res.rate
        super().save(*args, **kwargs)




class Payment(models.Model):
    reservation_pay = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    METHOD_PAY=(
        ('1','Paypal'),
    )
    method = models.CharField(max_length=50,choices=METHOD_PAY)




    