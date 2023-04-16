from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from movies.models import Movie
from movies.serializer import MovieSerializer
from django.forms.models import model_to_dict

# Create your views here.
class MovieView(APIView): 
    def get(self, request: Request):
        movies = Movie.objects.all()
        serialized = MovieSerializer(movies, many=True)

        return Response(serialized.data)

    def post(self, request: Request):
        serialized = MovieSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.validated_data, status.HTTP_201_CREATED)
    
class MovieByIdView(APIView):
    def get(self, request: Request, movie_id):
        find_movie = Movie.objects.filter(id=movie_id).first()
        serialized = MovieSerializer(find_movie)

        return Response(serialized.data, status.HTTP_200_OK)