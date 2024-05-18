from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    MEMBER = 'user'


class Employee(AbstractUser):
    """Создаем класс сотрудника"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя пользователя', null=True, blank=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия пользователя', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    image = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name="Active")
    supplier = models.BooleanField(default=False, verbose_name="поставщик")

    role = models.CharField(max_length=15, verbose_name='роль', choices=UserRole.choices, default=UserRole.MEMBER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['is_active', ]
