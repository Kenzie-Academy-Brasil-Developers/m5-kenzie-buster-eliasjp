from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView, Request, Response, status
from users.serializer import UserSerializer
from users.models import User
from users.permissions import IsAdminUser, IsOwnerOrAdmin
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
    permission_classes = [IsOwnerOrAdmin]
    
    def get(self, request, user_id):
        find_user = User.objects.filter(id=user_id).first()
        self.check_object_permissions(request, find_user)
        serialized = UserSerializer(instance=find_user)

        return Response(serialized.data, status.HTTP_200_OK)

    def patch(self, request, user_id):
        find_user = User.objects.filter(id=user_id).first()
        self.check_object_permissions(request, find_user)
        serialized = UserSerializer(find_user, request.data, partial=True)
        serialized.is_valid()
        serialized.save()

        return Response(serialized.data, status.HTTP_200_OK)