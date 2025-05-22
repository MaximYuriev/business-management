from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "company",
            "password",
            "position",
        ]
