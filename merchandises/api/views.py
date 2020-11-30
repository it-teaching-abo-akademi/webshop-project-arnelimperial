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
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import filters, pagination
import json
from django.http import JsonResponse
from django.core import serializers
from rest_framework import serializers
from django.contrib.auth import get_user_model

from purchases.models import Purchase
from .serializers import MerchandiseSerializer
from merchandises.models import Merchandise
from .permissions import IsVendorOrReadOnly

User = get_user_model()



class MerchandiseViewset(ModelViewSet):
    serializer_class = MerchandiseSerializer
    queryset = Merchandise.objects.all().order_by("-created_date")
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    lookup_field = "slug"
    permission_classes = [IsAuthenticated,IsVendorOrReadOnly,]
    search_fields = ['title',]
    filter_backends = (filters.SearchFilter,)

    def perform_create(self, serializer):
        serializer.save(merchant=self.request.user)

    # def update(self, request, *args, **kwargs):
    #     instance = Purchase.objects.filter(purchases=)
    #     for obj in instance:
    #         obj.purchases.item.on_stock = False
    #         obj.save()


class MerchandiseCountView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = MerchandiseSerializer
    queryset = Merchandise.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    permission_classes = [IsAdminUser]
    # lookup_field = "username"

    def list(self, request, *args, **kwargs):
        product_count = Merchandise.objects.all().count()
        content = {"product_count": product_count}
        return Response(content)


class MerchandiseOwnedByUserView(RetrieveModelMixin, UpdateModelMixin,GenericViewSet):
    serializer_class = MerchandiseSerializer
    queryset = Merchandise.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    permission_classes = [IsAuthenticated,IsVendorOrReadOnly]
    lookup_field = "slug"
    
    def list(self, request, *args, **kwargs):
        user = self.request.user
        v = Merchandise.objects.filter(merchant=user)
       
        product_owned_by_user = Merchandise.objects.filter(merchant=user).values('pk','title', 'slug','description', 'price', 'price_dec','product_image', 'created_date','updated_date', 'merchant',)
        return Response(product_owned_by_user)

    