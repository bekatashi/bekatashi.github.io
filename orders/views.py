from django.shortcuts import render
from .models import Order
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders import serializers


class OrdersViewSet(ModelViewSet):
    class Meta:
        fields = '__all__'
        model = Order
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

