# Generated by Django 4.0.3 on 2022-05-10 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_hotels_tour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='city',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='tour',
        ),
    ]
