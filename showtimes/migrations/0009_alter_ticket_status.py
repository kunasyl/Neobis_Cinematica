# Generated by Django 4.1.7 on 2023-05-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0008_alter_ticket_price_age_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Бронь', 'Reserved'), ('Куплено', 'Bought')], default='Бронь', max_length=50, verbose_name='Статус'),
        ),
    ]
