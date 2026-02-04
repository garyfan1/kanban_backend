from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) # to prevent other user creating someone else's
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        return User.objects.create_user(username=username, password=password)

    class Meta:
        model = User
        fields = ["id", "username", "password"]