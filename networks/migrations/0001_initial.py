# Generated by Django 5.0.4 on 2024-05-10 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер дома')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='networks.factory', verbose_name='Поставщик')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер дома')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='networks.individualentrepreneur', verbose_name='Поставщик')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер дома')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='networks.retailnetwork', verbose_name='Поставщик')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
