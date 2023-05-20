from rest_framework import serializers

from temporary.models import Temporary
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'password', 'repeat_password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomUserAdminSerializer(serializers.ModelSerializer):
    temporary = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['full_name', 'temporary']

    def get_temporary(self, obj):
        from temporary.serializers import TemporarySerializer

        temporaries = Temporary.objects.filter(user=obj)
        return TemporarySerializer(temporaries, many=True).data
