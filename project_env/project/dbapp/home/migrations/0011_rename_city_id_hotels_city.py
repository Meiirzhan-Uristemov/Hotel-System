# Generated by Django 4.0.3 on 2022-05-10 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_city_hotels_city_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotels',
            old_name='city_id',
            new_name='city',
        ),
    ]
