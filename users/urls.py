from rest_framework.urls import path
from users.views import UserView, LoginView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", LoginView.as_view())
]