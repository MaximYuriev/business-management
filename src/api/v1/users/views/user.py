from django.db.models import Avg
from rest_framework import viewsets

from api.v1.commons.permissions import IsSelfOrReadOnly
from api.v1.users.serializers import UserSerializer
from apps.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    Определяет эндпойнты для взаимодействия с пользователями.
    Регистрация новых пользователей и чтение уже добавленных доступно всем.
    Удаление и изменение полей доступно только владельцу аккаунта.
    """
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrReadOnly]

    def get_queryset(self):
        queryset = User.objects.all()

        if self.action == "list" or self.action == "retrieve":
            return User.objects.annotate(
                avg_task_rating=Avg("responsible_tasks__rating")
            ).prefetch_related("responsible_tasks")

        return queryset