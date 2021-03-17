from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from apps.palindrome.serializers import SubPalindrometSerializer
from apps.palindrome.palindrome_algorithm import get_sub_palindrome


class PalindromeAPIView(APIView):
    """
    Endpoint to get the substring palindrome.

    palindrome -- Query parameter with the string to evaluate
    """
    allowed_methods = ['GET']
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

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
