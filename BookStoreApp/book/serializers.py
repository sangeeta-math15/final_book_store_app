from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """
    create class BookSerializer
    modelSerializer:-set of fields and validators are  automatically created .
    """
    class Meta:
        model = Book
        # all fields in the model should be used.
        fields = '__all__'

    def create(self, validate_data):
        """
        for creating the books
        :param validate_data: validating the api data
        """
        books = Book.objects.create(
            author=validate_data.get("author"),
            title=validate_data.get("title"),
            quantity=validate_data.get("quantity"),
            price=validate_data.get("price"),
            description=validate_data.get("description")
        )
        return books
