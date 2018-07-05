# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_name', models.CharField(max_length=255)),
                ('carrier', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('eta', models.DateTimeField()),
                ('etd', models.DateTimeField()),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FlightBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('eta', models.DateTimeField()),
                ('etd', models.DateTimeField()),
            ],
        ),
    ]
