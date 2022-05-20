from rest_framework import serializers

from account.serializers import UserSerializer
from products.models import Product
from orders.models import Order
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
#     product = serializers.IntegerField()
#     count = serializers.IntegerField()

    class Meta:
        model = Order
        exclude = ('user',)
        # exclude = ('user',)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product).data
        # representation['user'] = instance.user.objects.get(user_id-instance.id)
        representation['user'] = UserSerializer(instance.user).data
        return representation


    # def validate(self, attrs):
    #     data = {}
    #     # user = attrs['user']
    #     try:
    #         product = Product.objects.get(pk=attrs['product'])
    #     except Product.DoesNotExist:
    #         raise serializers.ValidationError('Product not found')
    #     count = attrs['count']
    #     data['count'] = count
    #     data['product'] = product.pk
    #     return data
    #
    # def save(self, **kwargs):
    #     data = self.validated_data
    #     user = kwargs['user']
    #     product = Product.objects.get(pk=data['product'])
    #     Order.objects.create(product=product, user=user, count=data['count'])