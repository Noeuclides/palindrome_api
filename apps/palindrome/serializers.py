from rest_framework import serializers


class SubPalindrometSerializer(serializers.Serializer):
    palindrome = serializers.CharField()
    sub_palindrome = serializers.CharField()