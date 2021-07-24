from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=10, write_only=True)
    password2 = serializers.CharField(
        help_text="Confirm Password", min_length=10, write_only=True
    )

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def create(self, validated_data):
        password = validated_data.get("password")
        password2 = validated_data.get("password2")

        if password == password2:
            password = validated_data.pop("password")

            validated_data.pop(
                "password2"
            )  # remove password2 from the dictionary because we dont need it anymore
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user
        else:
            raise ValidationError("Password doesn't match")
