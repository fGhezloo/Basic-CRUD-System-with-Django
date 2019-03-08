from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes


class OrdersView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data})

    def post(self, request):
        order = request.data.get('order')
        serializer = OrderSerializer(data=order)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order '{}' created successfully".format(order_saved.purchaseID)})


    def put(self, request, pk):
        saved_order = get_object_or_404(Order.objects.all(), pk=pk)
        data = request.data.get('order')
        serializer = OrderSerializer(instance=saved_order, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
        	order_saved = serializer.save()
        return Response({"success": "Order '{}' updated successfully".format(order_saved.purchaseID)})

    def delete(self, request, pk):
        order = get_object_or_404(Order.objects.all(), pk=pk)
        order.delete()
        return Response({"message": "Order with id '{}' has been deleted.".format(pk)},status=204)
