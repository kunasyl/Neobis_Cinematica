# Generated by Django 4.1.7 on 2023-05-21 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0003_ticket_status_ticket_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtime',
            name='tickets_sold',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество проданных билетов'),
        ),
    ]
