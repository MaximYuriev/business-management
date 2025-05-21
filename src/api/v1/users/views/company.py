from rest_framework import viewsets

from api.v1.commons.permissions import IsAdminOrReadOnly
from api.v1.users.serializers import CompanySerializer
from apps.users.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrReadOnly]
