from rest_framework.permissions import BasePermission


class IsOwnerHabit(BasePermission):
    """Класс разрешения. Проверяет, что пользователь является владельцем объекта"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
