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

    
