from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.commons.permissions import IsManagerOrReadOnly
from api.v1.users.serializers import MeetingSerializer
from apps.users.models import Meeting


class MeetingViewSet(viewsets.ModelViewSet):
    """
    Определяет эндпойнты для управления встречами.
    Чтение доступно всем аутентифицированным пользователям.
    Добавление, удаление и изменение только менеджерам.
    """
    queryset = Meeting.objects.prefetch_related("employees")
    serializer_class = MeetingSerializer
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]
