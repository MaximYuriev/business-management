from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.commons.permissions import TaskPermission
from api.v1.users.serializers import TaskSerializer
from apps.users.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    """
    Определяет эндпойнты для управления задачами.
    Доступ имеют только аутентифицированные пользователи.
    Чтение разрешено всем аутентифицированные пользователям.
    Добавление и удаление только менеджерам.
    Изменение определенных полей разрешается подчиненному, для которого была определена задача.
    Изменение остальных данных разрешено только менеджерам.
    """
    queryset = Task.objects.select_related("author", "responsible")
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, TaskPermission]
