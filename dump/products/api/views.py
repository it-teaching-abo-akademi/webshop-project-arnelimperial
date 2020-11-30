from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
#from datetime import timedelta, datetime
# from django.http import Http404, HttpResponse
# from rest_framework.generics import CreateAPIView
# from rest_framework.exceptions import APIException
# from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags


from .serializers import ProductSerializer
from products.models import Product

class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductCountView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    permission_classes = [IsAdminUser]
    # lookup_field = "username"

    def list(self, request, *args, **kwargs):
        product_count = Product.objects.all().count()
        content = {"product_count": product_count}
        return Response(content)
    