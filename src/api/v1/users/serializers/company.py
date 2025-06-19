from rest_framework import serializers

from apps.users.models import Company, User


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "position",
        ]


class CompanySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "employees",
        ]
