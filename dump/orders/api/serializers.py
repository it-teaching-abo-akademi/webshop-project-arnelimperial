from rest_framework import serializers
from orders.models import Cart


class CartSerializer(serializers.ModelSerializer):
    buyer = serializers.StringRelatedField(read_only=True)
    
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['buyer', 'item', 'quantity', 'sold', 'created_date', 'cost']


    def get_created_date(self, instance):
        return instance.created_date.strftime('%B %d %Y')

    