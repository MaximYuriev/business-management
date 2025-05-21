from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Разрешает чтение всем, а запись только администраторам.
    """

    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        return request.user and request.user.is_staff