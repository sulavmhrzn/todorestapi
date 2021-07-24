from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "id",
            "url",
            "title",
            "description",
            "is_completed",
            "user",
            "date_started",
            "date_completed",
        ]
        read_only_fields = ["user", "date_completed"]
