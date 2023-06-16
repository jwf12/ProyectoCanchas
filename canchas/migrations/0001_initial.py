# Generated by Django 4.2.2 on 2023-06-09 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_court', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
                ('court_type', models.CharField(choices=[(1, 'Cemento'), (2, 'Sintetico'), (3, 'Parquet')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('age', models.DateField(auto_now=True)),
                ('sex', models.CharField(choices=[(1, 'Female'), (2, 'Male')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField()),
                ('status', models.CharField(choices=[(1, 'Disponible'), (2, 'Reservado')], default=1, max_length=50)),
                ('court_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.court')),
                ('day_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.day')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=6, max_length=6, prefix='')),
                ('court_res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.court')),
                ('player_res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.player')),
                ('shift_res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.shift')),
                ('sport_res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.sports')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[(1, 'Paypal')], max_length=50)),
                ('reservation_pay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.reservation')),
            ],
        ),
        migrations.AddField(
            model_name='court',
            name='sport_court',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.sports'),
        ),
    ]