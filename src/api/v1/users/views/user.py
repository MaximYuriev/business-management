from rest_framework import viewsets

from api.v1.commons.permissions import IsSelfOrReadOnly
from api.v1.users.serializers import UserSerializer
from apps.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrReadOnly]
