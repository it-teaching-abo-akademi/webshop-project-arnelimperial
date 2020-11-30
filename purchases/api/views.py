from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status, pagination
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from django.db.models import Sum, Avg, Count

from .serializers import PurchaseSerializer
##from .permissions import IsNotVendor
from purchases.models import Purchase
from merchandises.models import Merchandise


class PurchaseViewset(ModelViewSet):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)
       
       
    def create(self, request, *args, **kwargs):
       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # def update(self, request, *args, **kwargs):
    #     instance = Purchase.objects.all()
    #     for obj in instance:
    #         obj.purchases.item.on_stock = False
    #         obj.save()


    

class PurchasesByUserView(ListModelMixin, RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    serializer_class = PurchaseSerializer
    #queryset = Cart.objects.annotate(items=Count('item'), price=Sum('item_price_dec'))
    queryset = Purchase.objects.all()
    #pagination_class = None
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    permission_classes = [IsAuthenticated]
    
   
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        user = self.request.user
        purchases_by_user = Purchase.objects.filter(buyer=user).values()
        # 'pk', 'item', 'customer', 'price', 'price_dec', 'merchant', 'merchant_email', 'created'
        return Response(purchases_by_user)

    # def destroy(self, request, *args, **kwargs):
    #     user = self.request.user
    #     cart_owned_by_user = Cart.objects.filter(customer=user)
    #     # instance = self.get_object()
    #     # self.perform_destroy(user)
    #     delete_user_obj = cart_owned_by_user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
       


    # # Delete all objects
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class BuyerPurchasesViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,]
    
    
    
    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(buyer=user)
    
    def pre_save(self, obj):
        obj.buyer = self.request.user
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        user = self.request.user
        
        v = Purchase.objects.filter(buyer=user)
       
        purchases = Purchase.objects.filter(buyer=user).values('id', 'purchases','buyer','buyer_username','sellers','purchases_price', 'created', 'purchased_item_name','purchased_item_description','purchased_item_product_image', 'on_stock')
        return Response(purchases)
      


class ItemBySellersViewSet(ModelViewSet):
    serializer_class = PurchaseSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,]
    
    
    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(sellers=user)
    
    def pre_save(self, obj):
        obj.sellers = self.request.user
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        user = self.request.user
        
        v = Purchase.objects.filter(sellers=user)
       
        sells = Purchase.objects.filter(sellers=user).values('id', 'purchases','buyer','buyer_username', 'sellers','purchases_price', 'created', 'purchased_item_name','purchased_item_description','purchased_item_product_image', 'on_stock')
        return Response(sells)
      

    