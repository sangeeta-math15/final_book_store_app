import random
import logging
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .models import User
from .models import UserOTP
from django.core.mail import send_mail
from .util import Email, EncodeDecodeToken, VerifyToken

logger = logging.getLogger('django')


class RegisterView(APIView):
    """
    This api is for registration of new user
    """
    def post(self, request):
        """@param request: username,email and password
        @return: it will return the registered user with its credentials
        """
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = User.objects.filter(username=serializer.data['username'])
            if user:
                return Response({"message": "User Already Registered"},
                                status=status.HTTP_400_BAD_REQUEST)
            new_user = User.objects.create_user(username=serializer.data['username'],
                                                password=serializer.data['password'],
                                                email=serializer.data['email'],
                                                phone=serializer.data['phone'],
                                                )

            user_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=new_user, otp=user_otp)
            mess = f"Hello {new_user.username},\nYour OTP is {user_otp}\nThanks!"
            send_mail(
                "Welcome to Book Store Application - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [new_user.email],
                fail_silently=False
            )
            return Response({"message": "OTP Sent to the user "}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"Error": "Failed to send otp"}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(APIView):
    """
    create verifyOTP class
    This api is for verification of email to this application
    """
    def get(self, request):
        """
        :param request: once the account verification link is clicked by user this will take that request
        :return: it will return the response of email activation
        """
        otp = request.data.get('otp')
        try:
            otp_obj = UserOTP.objects.get(otp=otp)
            user = User.objects.get(id=otp_obj.user_id)
            if not user.is_active:
                user.is_active = True
                user.save()
            logger.info("Email Successfully Verified")
            return Response({'message': 'Successfully activated'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response({'error': 'Something Went Wrong'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    This class creates login api and validate user based on details.
    Returns response of login success or fail.
    """

    def post(self, request):
        """
        :param request: username and password
        :return: login success or fail.
        """
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user:
                encoded_token = EncodeDecodeToken().encode_token(data=user.pk)
                return Response(
                    {
                        "message": "logged in successfully",
                        "data": {"token": encoded_token}
                    }, status=status.HTTP_202_ACCEPTED)

        except AuthenticationFailed:
            return Response("Exception: Authentication failed..", status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({'Exception': str(e)})
