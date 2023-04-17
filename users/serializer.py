from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator

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
            