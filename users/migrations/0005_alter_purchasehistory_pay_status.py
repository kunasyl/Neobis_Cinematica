# Generated by Django 4.1.7 on 2023-05-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_purchasehistory_price_alter_discount_discount_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasehistory',
            name='pay_status',
            field=models.CharField(choices=[('Оплачено', 'Paid')], max_length=50, verbose_name='Статус покупки'),
        ),
    ]
