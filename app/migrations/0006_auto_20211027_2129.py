# Generated by Django 3.1.6 on 2021-10-27 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_buyorders_paymentpethod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyorders',
            old_name='paymentpethod',
            new_name='paymentMethod',
        ),
    ]
