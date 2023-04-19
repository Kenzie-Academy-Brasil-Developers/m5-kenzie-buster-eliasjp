from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView, Request, Response, status
from users.serializer import UserSerializer
from users.models import User
from users.permissions import IsAdminUser, IsOwner
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class UserView(APIView):
    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        serialized.save(is_superuser=serialized.validated_data["is_employee"])
        return Response(serialized.data, status.HTTP_201_CREATED)
    
class UserByIdView(APIView):
    authentication_classes = [JWTAuthentication]
    def get_permissions(self):
        if self.request.method == "PATCH":
            return [IsOwner()]
        return super().get_permissions()

    def patch(self, request, user_id):
        return Response("oi")