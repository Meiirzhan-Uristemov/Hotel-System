# Generated by Django 4.0.3 on 2022-05-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('card_number', models.CharField(blank=True, max_length=50, null=True)),
                ('balance', models.BigIntegerField(blank=True, null=True)),
                ('card_cvv', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HotelOrders',
            fields=[
                ('order_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('total_balance', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hotel_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('hotel_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('hotel_photo', models.CharField(blank=True, max_length=50, null=True)),
                ('hotel_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('hotel_price', models.BigIntegerField(blank=True, null=True)),
                ('city_id', models.BigIntegerField(blank=True, null=True)),
                ('tour_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hotels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('tour_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tour_name', models.CharField(blank=True, max_length=50, null=True)),
                ('tour_description', models.CharField(blank=True, max_length=50, null=True)),
                ('tour_price', models.BigIntegerField(blank=True, null=True)),
                ('tour_photo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tour',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TourOrders',
            fields=[
                ('order_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('total_balance', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tour_orders',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
