from django.urls import path
from .views import RegisterView, VerifyOTP, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('otp-verify/', VerifyOTP.as_view(), name='otp-verify'),
    path('login', LoginView.as_view(), name='login'),
    # path('validate', ValidateToken.as_view(), name='validate')
    # path(r'^/validate/(?P<token>[A-Za-z0-9][.])/$', ValidateToken.as_view(), name='validate')
]