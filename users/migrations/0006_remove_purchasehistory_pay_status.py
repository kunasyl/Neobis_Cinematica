# Generated by Django 4.1.7 on 2023-05-28 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_purchasehistory_pay_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='pay_status',
        ),
    ]
