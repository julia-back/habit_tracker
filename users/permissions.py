from rest_framework.permissions import BasePermission


class IsOwnerProfile(BasePermission):
    """Класс разрешения. Проверяет, что объект модели пользователя является текущим пользователем."""

    def has_object_permission(self, request, view, obj):
        return request.user == obj
