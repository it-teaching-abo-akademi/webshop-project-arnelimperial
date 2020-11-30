from rest_framework import serializers
from purchases.models import Purchase
from merchandises.models import Merchandise
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator
from django.db.models import Sum, Avg, Count

class PurchaseSerializer(serializers.ModelSerializer):
    purchased_item_name = serializers.SerializerMethodField()
    purchased_item_description = serializers.SerializerMethodField()
    purchased_item_product_image = serializers.SerializerMethodField()
    #purchased_item_slug = serializers.SerializerMethodField()
    buyer = serializers.StringRelatedField()
    sellers = serializers.StringRelatedField()
    purchases_price = serializers.StringRelatedField()
    buyer_email = serializers.SerializerMethodField()
    on_stock = serializers.SerializerMethodField()
    #_price = serializers.SerializerMethodField()
    purchases_price_dec = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        fields = ['purchases','buyer','buyer_email','buyer_username','sellers','purchases_price', 'created', 'purchased_item_name','purchased_item_description','purchased_item_product_image','url', 'on_stock', 'purchases_price_dec']
        
        extra_kwargs = {
            "url": {"view_name": "api:purchases-detail", "lookup_field": "id"}
        }

    
    def get_purchased_item_name(self, instance):
        return instance.purchases.item.title
      
    def get_buyer_email(self, instance):
        return instance.purchases.customer.email

    def get_purchased_item_description(self, instance):
        return instance.purchases.item.description
        
    def get_purchased_item_product_image(self, instance):
        return instance.purchases.item.product_image
    
    def get_purchases_price_dec(self, instance):
        return instance.purchases.item.price_dec
    
    def get_on_stock(self, instance):
        return instance.on_stock

    def get_created(self, instance):
        return instance.created.strftime('%B %d %Y')
    
    

    

    



    