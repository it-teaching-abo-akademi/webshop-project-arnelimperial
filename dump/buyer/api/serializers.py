from rest_framework import serializers
from buyer.models import ProductBought


class ProductBoughtSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductBought
        fields = ['product_name', 'created_date', 'updated_date',]

    