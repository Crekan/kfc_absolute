from rest_framework import serializers

from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'password', 'repeat_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
