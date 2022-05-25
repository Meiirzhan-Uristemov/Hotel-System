# Generated by Django 4.0.4 on 2022-04-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.BigIntegerField(blank=True, null=True, primary_key=True, serialize=False)),
                ('student_first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student_email', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('balance', models.BigIntegerField(blank=True, null=True)),
                ('exam_score', models.BigIntegerField(blank=True, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'students',
                'managed': True,
            },
        ),
    ]
