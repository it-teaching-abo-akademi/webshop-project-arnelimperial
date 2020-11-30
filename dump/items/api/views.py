from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
#from datetime import timedelta, datetime
from django.http import Http404, HttpResponse
#from rest_framework.generics import CreateAPIView
# from rest_framework.exceptions import APIException
# from django.core.mail import send_mail, send_mass_mail, EmailMessage, EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework import filters

from .serializers import ItemSerializer
from items.models import Item
from .permissions import IsVendorOrReadOnly



class ItemViewset(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().order_by("-created_date")
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    lookup_field = "slug"
    permission_classes = [IsAuthenticated,IsVendorOrReadOnly]
    search_fields = ['title',]
    filter_backends = (filters.SearchFilter,)

    # def perform_create(self, serializer):
    #     serializer.save(vendor=self.request.user)


class ItemCountView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    permission_classes = [IsAdminUser]
    # lookup_field = "username"

    def list(self, request, *args, **kwargs):
        product_count = Item.objects.all().count()
        content = {"product_count": product_count}
        return Response(content)

import json
from django.http import JsonResponse
from django.core import serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemOwnedByUserView(RetrieveModelMixin, GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    permission_classes = [IsAuthenticated]
    # lookup_field = "username"


    def list(self, request, *args, **kwargs):
        user = self.request.user
        v = Item.objects.filter(vendor=user)
       
        product_owned_by_user = Item.objects.filter(vendor=user).values('pk','title', 'slug','description', 'price', 'product_image', 'created_date','updated_date', 'vendor')
        return Response(product_owned_by_user)

    