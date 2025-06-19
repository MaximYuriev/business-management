from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    avg_task_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "company",
            "password",
            "position",
            "avg_task_rating"
        ]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            company=validated_data["company"],
            position=validated_data["position"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
