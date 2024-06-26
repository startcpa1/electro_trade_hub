# Generated by Django 5.0.4 on 2024-05-16 23:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0004_alter_factory_supplier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='networks.factory', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='individualentrepreneur',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='networks.individualentrepreneur', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='retailnetwork',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='networks.retailnetwork', verbose_name='Поставщик'),
        ),
    ]
