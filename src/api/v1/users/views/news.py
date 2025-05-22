from rest_framework import viewsets

from api.v1.commons.permissions import IsAdminOrReadOnly
from api.v1.users.serializers import NewsSerializer
from apps.users.models import News


class NewsViewSet(viewsets.ModelViewSet):
    """
    Определяет эндпойтны для взаимодействия с новостями.
    Чтение доступно всем пользователям, добавление, изменение и удаление - админам.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]
