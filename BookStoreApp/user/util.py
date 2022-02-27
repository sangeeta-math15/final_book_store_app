import logging
import jwt
from rest_framework.response import Response
from django.core.mail import send_mail
from BookStoreApp import settings


class Email:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()


class EncodeDecodeToken:
    """
    create class EncodeDecodeToken
+   """
    def encode_token(self, data):
        """
        :param data:request data
        :return:encoded_token
        """
        encoded_token = jwt.encode({data: data}, "secret", algorithm="HS256")
        return encoded_token

    def decode_token(self, encoded_token):
        """
        :param encoded_token:request the encoded_token
        :return:decoded token
        """
        decoded_token = jwt.decode(encoded_token, "secret", algorithms="HS256")
        return decoded_token


class VerifyToken:
    """
    create class VerifyToken
    """
    def verify_token(self, request):
        """
         Given request, extract token and decode it to verify
        :param request:
        :return:boolen value
        """
        token = request.META['HTTP_AUTHORIZATION']
        tkn_data = EncodeDecodeToken().decode_token(token)
        if tkn_data:
            return True
        return False
