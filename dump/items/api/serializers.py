from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    created_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()
    # user_sold_count = serializers.SerializerMethodField()
    # buyers_count = serializers.SerializerMethodField()
    #item_created_count = serializers.SerializerMethodField()
    #products = serializers.PrimaryKeyRelatedField(read_only=True)
   
    class Meta:
        model = Item
        fields = '__all__'
        # exclude = ['slug']

    def get_created_date(self, instance):
        return instance.created_date.strftime('%B %d %Y')

    def get_updated_date(self, instance):
        return instance.updated_date.strftime('%B %d %Y')

    # def get_item_created_count(self, instance):
    #     request = self.context.get('request')
    #     #return Item.objects.all().count()
        
       
    
    # def get_user_sold_count(self, instance):
    #     request = self.context.get('request')
    #     return instance.buyers.filter(pk=request.user.pk).exist()

    # def get_buyers_count(self, instance):
    #     return instance.buyers.count()

    # def get_user_has_answered(self, instance):
    #     request = self.context.get("request")
    #     seller = instance.answers.filter(vendor=request.user).exists()

  



    

    