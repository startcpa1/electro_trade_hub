from django.contrib import admin

from users.models import Employee

"""Регистрация модели Employee в административной панели"""
admin.site.register(Employee)
