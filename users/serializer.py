from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")])
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        
        if validated_data.get("password"):
            validated_data["password"] = make_password(validated_data["password"])
            instance.password = validated_data.get("password", instance.password)

        instance.save()
        return instance