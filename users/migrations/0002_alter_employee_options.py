# Generated by Django 5.0.4 on 2024-05-17 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['is_active'], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
