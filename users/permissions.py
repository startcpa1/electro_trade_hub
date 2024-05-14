from rest_framework.permissions import BasePermission

from users.models import UserRole


class IsAdmin(BasePermission):
    """Проверяем права администратора"""

    def has_permission(self, request, view):
        return request.user.role == UserRole.ADMIN


class IsOwner(BasePermission):
    """Проверяем права автора"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsProfileUser(BasePermission):
    """Проверяем права владельца"""

    def has_object_permission(self, request, view, obj):
        return request.user.email == obj.email
