from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from users.serializer import UserSerializer
from users.models import User
from django.forms.models import model_to_dict

# Create your views here.
class UserView(APIView):
    def get(self, request: Request):
        return Response("chamada", status.HTTP_200_OK)
    
    def post(self, request: Request):
        serialized = UserSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        find_email = User.objects.filter(email=request.data["email"]).first()
        if find_email:
            return Response({"username": [request.data["username"]], "email": ["email already taken."]}, status.HTTP_400_BAD_REQUEST)
        find_user = User.objects.filter(username=request.data["username"]).first()
        if find_user:
            return Response({"username": ["username already taken."], "email": [request.data["email"]]}, status.HTTP_400_BAD_REQUEST)
        
        serialized.save(is_superuser=serialized.validated_data["is_employee"])
        return Response(serialized.data, status.HTTP_201_CREATED)