from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelfOrReadOnly(BasePermission):
    """
    Разрешает чтение всем, а запись, удаление и редактирование только владельцам.
    """

    def has_object_permission(self, request, view, obj):
        if request.method is SAFE_METHODS:
            return True

        return obj == request.user
