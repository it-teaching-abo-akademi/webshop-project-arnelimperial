from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



from .serializers import InitialSerializer
from initial.models import Initial

class InitialViewset(ModelViewSet):
    serializer_class = InitialSerializer
    queryset = Initial.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser]


# from datetime import timedelta, datetime
# from django.http import Http404, HttpResponse
# from rest_framework.generics import CreateAPIView
# from rest_framework.exceptions import APIException
# from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags