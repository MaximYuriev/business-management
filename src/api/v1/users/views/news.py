from rest_framework import viewsets

from api.v1.commons.permissions import IsAdminOrReadOnly
from api.v1.users.serializers import NewsSerializer
from apps.users.models import News


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]
