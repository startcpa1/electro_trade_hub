# Generated by Django 5.0.4 on 2024-05-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networks', '0007_remove_individualentrepreneur_supplier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networknode',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность(Руб)'),
        ),
    ]