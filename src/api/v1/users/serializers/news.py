from rest_framework import serializers

from apps.users.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        field = "__all__"
