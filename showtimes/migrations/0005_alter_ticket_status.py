# Generated by Django 4.1.7 on 2023-05-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0004_showtime_tickets_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(blank=True, choices=[('Бронь', 'Reserved'), ('Куплено', 'Bought'), ('Возвращено', 'Returned')], default='Бронь', max_length=50, null=True, verbose_name='Статус'),
        ),
    ]