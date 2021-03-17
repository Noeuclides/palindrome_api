from django.urls import path, include
from apps.users.api.api import (
    UserAPIView, UserDetailAPIView, LoginAPIView, UserRetrieveView
)


urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('user/<int:pk>/', UserDetailAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('auth/user', UserRetrieveView.as_view()),
    path('register', UserAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    # path('logout', LogoutView.as_view(), name='knox_logout')
]