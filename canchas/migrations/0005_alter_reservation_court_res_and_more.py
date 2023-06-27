# Generated by Django 4.2.2 on 2023-06-27 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0004_alter_shift_day_shift_delete_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='court_res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.sports'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='sport_res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canchas.court'),
        ),
    ]
