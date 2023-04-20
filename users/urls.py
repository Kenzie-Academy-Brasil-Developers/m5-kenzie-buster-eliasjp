from rest_framework.urls import path
from users.views import UserView, UserByIdView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserByIdView.as_view()),
    path("users/login/", TokenObtainPairView.as_view())
]