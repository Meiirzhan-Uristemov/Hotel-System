# Generated by Django 4.0.3 on 2022-05-10 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_card_city_country_hotelorders_hotels_tour_tourorders_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='hotelorders',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='hotels',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tourorders',
            options={'managed': True},
        ),
    ]
