from rest_framework import serializers

from api.v1.users.serializers.company import EmployeeSerializer
from apps.users.models import Meeting, User


class MeetingSerializer(serializers.ModelSerializer):
    employees_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=User.objects.all(),
        source="employees",
    )
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = "__all__"
