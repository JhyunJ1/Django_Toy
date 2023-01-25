from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Order
from .serializers import OrderSerializer
from .paginations import OrderLargePagination

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination

    def get_queryset(self):
        order = Order.objects.all()
        return order
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        pass