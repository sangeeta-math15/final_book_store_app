from django.core.mail import send_mail
from BookStoreApp import settings


# class Email:
#     @staticmethod
#     def send_email( to,token,name ):
#         send_mail(from_email=settings.EMAIL_HOST, recipient_list=[to],
#                   message="Hy {}\n Welcome to Fundonotes App ,Thanks for installing our software\n Your Activation url = "
#                           "http://127.0.0.1:8000/user/validate/{}".format( name,
#                       token),
#                   subject="Link for Your Registration", fail_silently=False, )

class Email:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
