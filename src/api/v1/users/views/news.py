from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.commons.permissions import IsManagerOrReadOnly
from api.v1.users.serializers import NewsSerializer
from apps.users.models import News


class NewsViewSet(viewsets.ModelViewSet):
    """
    Определяет эндпойтны для взаимодействия с новостями.
    Чтение доступно всем аутентифицированным пользователям.
    Добавление, изменение и удаление - менеджерам.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]
