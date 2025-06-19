from rest_framework import serializers

from apps.users.models import Task, User
from .company import EmployeeSerializer


class TaskSerializer(serializers.ModelSerializer):
    author = EmployeeSerializer(read_only=True)
    responsible = EmployeeSerializer(read_only=True)
    responsible_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='responsible',
    )

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user

        task = Task.objects.create(**validated_data)

        return task
