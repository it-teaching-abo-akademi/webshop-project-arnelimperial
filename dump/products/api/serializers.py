from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    #slug = serializers.SlugField()
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()
    # user_sold_count = serializers.SerializerMethodField()
   
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['slug']

    def get_created_date(self, instance):
        return instance.created_date.strftime('%B %d %Y')

    def get_updated_date(self, instance):
        return instance.updated_date.strftime('%B %d %Y')
    
    # def get_user_sold_count(self, instance):
    #     request = self.context.get('request')
    #     return instance.buyer.filter(pk=request.user.pk).exist()

    

    