# Generated by Django 4.1.7 on 2023-05-28 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_discount_tickets_bought'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseHistory',
        ),
    ]
