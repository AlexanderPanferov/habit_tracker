from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Класс для проверки пользователя"""
    message = 'Вы не владелец!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
