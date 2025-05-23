from rest_framework.permissions import BasePermission, SAFE_METHODS


class TaskPermission(BasePermission):
    """
    Разрешает чтение всем пользователям.
    Добавление и удаление только менеджерам.
    Изменение определенных полей разрешается подчиненному, для которого была определена задача.
    Изменение остальных данных разрешено только менеджерам.
    """

    SUBORDINATE_EDITABLE_FIELDS = ["status"]

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method in "POST":
            return request.user.check_is_manager()

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.method in "DELETE":
            return request.user.check_is_manager()

        if request.method in ["PUT", "PATCH"]:
            if request.user.check_is_manager():
                return True

            if request.user == obj.responsible:
                return all(field in self.SUBORDINATE_EDITABLE_FIELDS for field in request.data)

        return False
