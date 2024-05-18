from django.core.management import BaseCommand

from users.models import Employee


class Command(BaseCommand):
    """Создаем суперпользователя"""
    def handle(self, *args, **options):
        user = Employee.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()
