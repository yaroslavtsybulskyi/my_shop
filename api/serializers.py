from rest_framework import serializers
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')
Basket = get_model('basket', 'Basket')
Order = get_model('order', 'Order')


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model from Oscar."""

    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    """Serializer for the Basket model from Oscar."""

    class Meta:
        model = Basket
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model from Oscar."""

    class Meta:
        model = Order
        fields = '__all__'
