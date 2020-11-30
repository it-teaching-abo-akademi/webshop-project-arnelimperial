from rest_framework import serializers
from carts.models import Cart
from merchandises.models import Merchandise
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator
from django.db.models import Sum, Avg, Count

class CartSerializer(serializers.ModelSerializer):
    item_name = serializers.SerializerMethodField()
    customer = serializers.StringRelatedField()
    customer_email = serializers.SerializerMethodField()
    merchant = serializers.StringRelatedField()
    item_price = serializers.SerializerMethodField()
    item_price_dec = serializers.SerializerMethodField()
    item_merchant_email = serializers.SerializerMethodField()
    on_stock = serializers.SerializerMethodField()

    created = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    
    def get_item_name(self, instance):
        return instance.item.title
      
    def get_customer_email(self, instance):
        return instance.customer.email

    def get_item_merchant(self, instance):
        return instance.item.merchant.username

    def get_item_merchant_email(self, instance):
        return instance.item.merchant.email

    def get_item_price(self, instance):
        return instance.item.price
    
    def get_item_price_dec(self, instance):
        return instance.item.price_dec
    
    def get_on_stock(self, instance):
        return instance.item.on_stock
    

    def get_created(self, instance):
        return instance.created.strftime('%B %d %Y')
    
    # def get_total_pieces(self, obj):
    #     totalpieces = Catalog.objects.all().aggregate(total_pieces=Count('no_of_pcs'))
    #     return totalpieces["total_pieces"]
    # def get_total_price(self, obj):
    #     totalprice = Catalog.objects.all().aggregate(total_price=Sum('per_piece_price'))
    #     return totalprice["total_price"]
    
    

    

    



    