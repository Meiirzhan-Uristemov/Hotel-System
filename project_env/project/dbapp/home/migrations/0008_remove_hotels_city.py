# Generated by Django 4.0.3 on 2022-05-10 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_hotels_city_id_remove_hotels_tour_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='city',
        ),
    ]