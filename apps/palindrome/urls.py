from django.urls import path, include
from apps.palindrome.views import PalindromeAPIView, HomeAPIView



urlpatterns = [
    path('palindrome', PalindromeAPIView.as_view()),
    path('', HomeAPIView.as_view()),
]