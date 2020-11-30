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

from .serializers import CartSerializer
from .permissions import IsNotVendor
from carts.models import Cart


class CartViewset(ModelViewSet):
    serializer_class = CartSerializer
    #queryset = Cart.objects.annotate(items=Count('item'), price=Sum('item_price_dec'))
    queryset = Cart.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,]
    #pagination_class = None
   

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, *args, **kwargs)
    #     user = self.request.user
    #     cart_owned_by_user = Cart.objects.filter(customer=user).values()
    #     # return Response(cart_owned_by_user)

     
    #     response.data['request_user_bill'] = list(Cart.objects.filter(customer=user).aggregate(Sum('item_price_dec')).values())[0]
    #     response.data['request_user_number_of_items'] = list(Cart.objects.filter(customer=user).aggregate(Count('item')).values())[0]
    #     response.data['total_items'] = list(Cart.objects.aggregate(Count('item')).values())[0]


    #     # response.data['Ave. Cost'] = list(Cart.objects.aggregate(Avg('item_price_dec')).values())[0]
    #     return response


class CartOwnedByUserView(ListModelMixin, RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    serializer_class = CartSerializer
    #queryset = Cart.objects.annotate(items=Count('item'), price=Sum('item_price_dec'))
    queryset = Cart.objects.all()
    pagination_class = None
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication,]
    permission_classes = [IsAuthenticated]
    
   
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        user = self.request.user
        cart_owned_by_user = Cart.objects.filter(customer=user).values('pk', 'item', 'customer', 'item_price', 'item_price_dec', 'merchant', 'created')
        return Response(cart_owned_by_user)

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        cart_owned_by_user = Cart.objects.filter(customer=user)
        delete_user_obj = cart_owned_by_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Delete all objects
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UserCartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    # queryset = Cart.objects.all()
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated,]
    # pagination_class = pagination.PageNumberPagination
    # pagination_class.page_size = 100
    

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(customer=user)
    
    def pre_save(self, obj):
        obj.customer = self.request.user
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        user = self.request.user
        costObj = list(Cart.objects.filter(customer=user).aggregate(Sum('item_price_dec')).values())[0]
        cost_str = str(costObj)
        cost = cost_str.replace('.', ',')

        response.data['bill'] = cost
        response.data['number_of_items'] = list(Cart.objects.filter(customer=user).aggregate(Count('item')).values())[0]
        return response

    