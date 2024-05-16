from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission

from users.models import UserRole


class IsAdmin(BasePermission):
    """Проверяем права администратора"""

    def has_permission(self, request, view):
        return request.user.role == UserRole.ADMIN


class IsProfileUser(BasePermission):
    """Проверяем права владельца"""

    def has_object_permission(self, request, view, obj):
        return request.user.email == obj.email


class UserIsActive(BasePermission):
    """Проверяем права сотрудника"""

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            raise PermissionDenied(detail='Доступ к api запрещен не активным сотрудникам.')
