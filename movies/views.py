from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from movies.serializer import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class MovieView(APIView, PageNumberPagination): 
    authentication_classes = [JWTAuthentication]
    def get_permissions(self):
        if self.request.method != "GET":
            return [IsAdminUser()]
        return super().get_permissions()

    def get(self, request: Request):
        find_movie = Movie.objects.all()
        result_page = self.paginate_queryset(find_movie, request, view=self)
        serialized = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serialized.data)

    def post(self, request: Request):
        serialized = MovieSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save(user=request.user)

        return Response(serialized.data, status.HTTP_201_CREATED)
    
    def delete(self, request: Request):
        find_movie = Movie.objects.filter(**request.data).first()
        if not find_movie:
            return Response({"detail": "Movie not found"}, status.HTTP_404_NOT_FOUND)
        find_movie.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
    
class MovieByIdView(APIView):
    authentication_classes = [JWTAuthentication]
    def get_permissions(self):
        if self.request.method != "GET":
            return [IsAdminUser()]
        return super().get_permissions()
    
    def get(self, request: Request, movie_id):
        find_movie = Movie.objects.filter(id=movie_id).first()
        serialized = MovieSerializer(instance=find_movie)

        return Response(serialized.data, status.HTTP_200_OK)
    

    def delete(self, request, movie_id):
        find_movie = Movie.objects.filter(id=movie_id).first()
        if not find_movie:
            return Response({"detail": "Movie not found"}, status.HTTP_404_NOT_FOUND)
        find_movie.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
    
class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, movie_id):
        serialized = MovieOrderSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        find_user = User.objects.filter(id=request.user.id).first()
        find_movie = Movie.objects.filter(id=movie_id).first()
        if not find_movie:
            return Response("Movie not found.", status.HTTP_404_NOT_FOUND)

        serialized.save(buyed_by=find_user, title=find_movie)

        return Response(serialized.data, status.HTTP_201_CREATED)