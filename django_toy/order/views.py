from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import Order, Comment
from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer
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

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer


    def get_queryset(self):
        return Order.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        return Comment.objects.filter(order_id=order_id)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
    mixins.DestroyModelMixin
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        return Comment.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    def delete(self, request, *args, **kwargs):
        pk = request.data.get('pk')
        if Comment.objects.filter(pk=pk).exists():
            comment = Comment.objects.get(pk=pk)
            comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

