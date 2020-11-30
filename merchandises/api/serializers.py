from rest_framework import serializers
from merchandises.models import Merchandise
from carts.models import Cart
from purchases.models import Purchase

class MerchandiseSerializer(serializers.ModelSerializer):
    #merchant = serializers.SerializerMethodField()
    #price_dec = serializers.StringRelatedField()
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()
    merchant_email = serializers.SerializerMethodField()
    merchant_username = serializers.SerializerMethodField()
    #on_stock = serializers.SerializerMethodField()
    # user_sold_count = serializers.SerializerMethodField()
    # buyers_count = serializers.SerializerMethodField()
    #item_created_count = serializers.SerializerMethodField()
    #products = serializers.PrimaryKeyRelatedField(read_only=True)

    
   
    class Meta:
        model = Merchandise
        #fields = '__all__'
        fields = ['id', 'title', 'slug', 'description', 'price', 'price_dec','merchant', 'created_date', 'updated_date', 'product_image', 'url', 'merchant_email', 'merchant_username', 'on_stock']
        read_only_fields = ('on_stock',)
        extra_kwargs = {
            "url": {"view_name": "api:merchandises-detail", "lookup_field": "slug"}
        }


    def get_created_date(self, instance):
        return instance.created_date.strftime('%B %d %Y')

    def get_updated_date(self, instance):
        return instance.updated_date.strftime('%B %d %Y')
    
    def get_merchant_email(self, instance):
        return instance.merchant.email
    
    def get_merchant_username(self, instance):
        return instance.merchant.username

    # def get_item_created_count(self, instance):
    #     request = self.context.get('request')
    #     #return Item.objects.all().count()
    
    # def get_on_stock(self, instance):
    #     request = self.context.get('request')
    #     return instance.buyers.filter(pk=request.user.pk).exist()

    # def get_on_stock(self, instance):

    #     return instance.__carts.__purchases.__on_stock
        

    # def get_user_has_answered(self, instance):
    #     request = self.context.get("request")
    #     seller = instance.answers.filter(vendor=request.user).exists()

  



    

    