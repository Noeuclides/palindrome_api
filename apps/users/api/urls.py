from django.urls import path, include
from apps.users.api.api import (
    UserAPIView, UserDetailAPIView, LoginAPIView, UserRetrieveView
)
from rest_framework_jwt.views import (
    obtain_jwt_token, refresh_jwt_token, verify_jwt_token
)
from rest_framework_jwt.blacklist.views import BlacklistView


urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('user/<int:pk>/', UserDetailAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('auth/user', UserRetrieveView.as_view()),
    path('register', UserAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('api-token-auth', obtain_jwt_token),
    path('api-token-refresh', refresh_jwt_token),
    path('api-token-verify', verify_jwt_token),
    path("logout", BlacklistView.as_view({"post": "create"}))
]