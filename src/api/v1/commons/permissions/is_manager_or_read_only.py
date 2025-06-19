from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagerOrReadOnly(BasePermission):
    """
    Разрешает чтение всем, а запись, редактирование и удаление только менеджерам.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.check_is_manager()
