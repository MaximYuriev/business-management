from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.commons.permissions import IsAdminOrReadOnly
from api.v1.users.serializers import CompanySerializer
from apps.users.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Определяет эндпойнты для взаимодействия с компаниями.
    Чтение данных о компании доступно всем аутентифицированным пользователям.
    Добавление, удаление и изменение данных о компании только админам.
    """
    queryset = Company.objects.prefetch_related("employees")
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
