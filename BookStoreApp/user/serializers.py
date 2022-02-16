
from rest_framework import serializers
from .models import User



class UserSerializer(serializers.Serializer):

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

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.id = validated_data.get('id', instance.id)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.is_verified = validated_data.get('is_verified', instance.is_verified)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance


