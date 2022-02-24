from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    """
    create UserSerializer class
    """
    username = serializers.CharField(allow_blank=False, allow_null=False, required=True)
    email = serializers.CharField(required=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    is_verified = serializers.BooleanField(default=False)
    phone = serializers.CharField(max_length=10, required=False)



    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)