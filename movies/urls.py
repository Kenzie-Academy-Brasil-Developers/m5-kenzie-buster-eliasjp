from rest_framework.urls import path
from movies.views import MovieView, MovieByIdView, MovieOrderView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieByIdView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view())
]