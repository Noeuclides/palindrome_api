from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from apps.palindrome.serializers import SubPalindrometSerializer
from apps.palindrome.utils import get_sub_palindrome


class PalindromeAPIView(APIView):
    allowed_methods = ['GET']

    def get(self, request: Request) -> Response:
        if not request.query_params:
            return Response(
                {'message': 'Query is missing'},
                status=status.HTTP_400_BAD_REQUEST)
        try:
            string = request.query_params.getlist('palindrome')[0]
            sub_palindrome = get_sub_palindrome(string)
            api_response = {
                'palindrome': string,
                'sub_palindrome': sub_palindrome
            }
            api_serielizer = SubPalindrometSerializer(api_response)
        except IndexError:
            return Response(
                {'message': 'The query parameter is palindrome'},
                status=status.HTTP_400_BAD_REQUEST)

        return Response(api_serielizer.data, status=status.HTTP_200_OK)


class HomeAPIView(APIView):
    allowed_methods = ['GET']

    def get(self, request: Request) -> Response:
        return Response(
            {'palindrome':
             'API that recognizes the longest palindrome within a text string'},
            status=status.HTTP_200_OK)
