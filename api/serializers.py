from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

# client serializer


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# status serializer


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

# profile serializer


class ProfileSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = ServiceProvider
        fields = '__all__'

    def get_status(self, obj):
        status_data = Status.objects.filter(owner_username=obj)
        data = StatusSerializer(status_data, many=True).data
        return data


# Register serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only':  True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

# login serializer


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_valid():
            return user
        raise serializers.ValidationError('incorrect credentials')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
