# Generated by Django 4.1.7 on 2023-05-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0007_alter_ticket_price_age_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='price_age',
            field=models.CharField(choices=[('Взрослый', 'Adult'), ('Детский', 'Child'), ('Студенческий', 'Student')], max_length=20, verbose_name='Ценовой возраст'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Бронь', 'Reserved'), ('Куплено', 'Bought'), ('Возвращено', 'Returned')], default='Бронь', max_length=50, verbose_name='Статус'),
        ),
    ]