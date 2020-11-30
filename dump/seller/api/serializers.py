from rest_framework import serializers
from seller.models import ProductSold 


class ProductSoldSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ProductSold
        fields = ['product_name', 'created_date']


    