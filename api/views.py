from rest_framework import viewsets
from .serializers import ProductSerializer, BasketSerializer, OrderSerializer
from oscar.apps.catalogue.models import Product
from oscar.apps.basket.models import Basket
from oscar.apps.order.models import Order


class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint that allows products to be viewed or edited."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """API endpoint that allows orders to be viewed or edited."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BasketViewSet(viewsets.ModelViewSet):
    """API endpoint that allows orders to be viewed or edited."""

    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
