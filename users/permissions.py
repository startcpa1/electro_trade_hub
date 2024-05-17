from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class UserIsActive(BasePermission):
    """Проверяем права активного сотрудника"""

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            raise PermissionDenied(detail='Доступ к api запрещен не активным сотрудникам.')
