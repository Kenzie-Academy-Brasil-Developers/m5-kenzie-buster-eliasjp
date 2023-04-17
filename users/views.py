from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView, Request, Response, status
from users.serializer import UserSerializer
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class UserView(APIView):
    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        serialized.save(is_superuser=serialized.validated_data["is_employee"])
        return Response(serialized.data, status.HTTP_201_CREATED)
    
class UserByIdView(APIView):
    ...