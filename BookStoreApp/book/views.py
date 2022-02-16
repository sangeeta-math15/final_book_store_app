from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, GenericAPIView, \
    RetrieveUpdateAPIView
from rest_framework.views import APIView

from rest_framework import permissions, status, views
import logging
from psycopg2 import OperationalError
from rest_framework.exceptions import ValidationError

logger = logging.getLogger('django')


class BookView(APIView):
    """
    curd operation
    """

    def post(self, request):
        """

        :param request:
        :return:
        """
        try:
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"Message": "data store successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error(e)
            return Response({"message": "validation failed"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            # print(request.GET.get("id"))
            # book = Book.objects.filter(id = request.GET.get("id"))
            book = Book.objects.filter(title = request.data['title'])

            print(book)
            # serializer = BookSerializer(book, many=True)
            # book = Book.objects.all()
            serializer = BookSerializer(book,many=True)
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
            print(request.data["id"])
            book = Book.objects.get(id=request.data["id"])
            print(book)
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
            note = Book.objects.get(id=request.data["id"])
            note.delete()
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
#
# class BookView(ListCreateAPIView):
#     serializer_class = BookSerializer
#
#     def perform_create(self, serializer):
#         """
#             This api is for creation of new books
#             @param request: title and description of notes
#             @return: response of created notes
#             :param serializer:
#             :param serializer:
#         """
#         try:
#             serializer.save()
#             return Response({'Message': 'Product Created Successfully'}, status=status.HTTP_200_OK)
#         except OperationalError as e:
#             logger.error(e)
#             return Response({'Message': 'Failed to connect with the database'}, status=status.HTTP_400_BAD_REQUEST)
#         except ValidationError as e:
#             logger.error(e)
#             return Response({'Message': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             logger.error(e)
#             return Response({'Message': 'Failed to create product'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def get_queryset(self):
#         try:
#
#             return Book.objects.all()
#         except OperationalError as e:
#             logger.error(e)
#             return Response({'Message': 'Failed to connect with the database'}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             logger.error(e)
#             return Response({'Message': 'Failed to get product'}, status=status.HTTP_400_BAD_REQUEST)
