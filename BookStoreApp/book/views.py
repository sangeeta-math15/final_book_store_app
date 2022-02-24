from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer
from rest_framework import status, views
import logging
from rest_framework.exceptions import ValidationError



logger = logging.getLogger('django')


class BookView(APIView):
    """
    curd operation
    """
    def post(self, request):
        """
        :param request: all fields in the model
        :return: book stored successfully or not
        """
        try:
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "book store successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error(e)
            return Response({"message": "validation failed"}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        """
        :return: get all books
        """
        try:
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response(
                {
                    "message": "Here your Book",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            logging.error(e)
            return Response(
                {
                    "message": "No book for you"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        this method is created for update the data
        :param request: format of the request
        :return: Response
        """
        try:
            print(request.data["title"])
            book = Book.objects.get(title=request.data["title"])
            serializer = BookSerializer(book, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Data updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            logging.error(e)
            return Response(
                {
                    "message": "Data not updated"
                },
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        this method is created for delete the book
        :param request:format of the request
        :return: response
        """
        try:
            book = Book.objects.get(title=request.data["title"])
            book.delete()
            return Response(
                {
                    "message": "Data deleted"
                },
                status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "Data not deleted"
                },
                status=status.HTTP_400_BAD_REQUEST)

