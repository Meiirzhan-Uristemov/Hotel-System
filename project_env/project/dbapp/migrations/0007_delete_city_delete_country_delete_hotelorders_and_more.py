# Generated by Django 4.0.3 on 2022-05-07 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0006_delete_registration_remove_users_card_id_delete_card_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='HotelOrders',
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
        migrations.DeleteModel(
            name='TourOrders',
        ),
    ]
