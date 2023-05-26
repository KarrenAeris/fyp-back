from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.parsers import FileUploadParser
from .serializers import OrderSerializer, OrderSerializerDetail

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user.models import User
from .models import Order
from .permissions import OrderPermission

# Create your views here.


class FileUploadView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [OrderPermission, ]
    
    def perform_create(self, serializer):
        print(serializer.validated_data['material_type'])
        p_material = {'ABS': 1.08, 'PLA': 1.25, 'PETG': 1.34, 'TPU': 1.25}
        m_material = {'ABS': 0.015, 'PLA': 0.018, 'PETG': 0.016, 'TPU': 0.027}
        p = p_material[serializer.validated_data['material_type']]
        m = m_material[serializer.validated_data['material_type']]
        c_material = serializer.validated_data['v_material'] * p * m
        trunning = serializer.validated_data['v_material'] / 30.15
        cenergy = 0.02 * trunning * 150
        coverhead = 2 * 1
        cprocessing = c_material + cenergy + coverhead
        cpre_processing = 2 * 2
        cprocess = cpre_processing + cprocessing
        ctotal = cprocess + 0.1 + cprocess
        serializer.save(user=self.request.user, price=ctotal)


class FileUploadViewList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [OrderPermission, ]


class FileUploadViewDetailCheck(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializerDetail
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [OrderPermission, ]


@api_view(['GET', 'POST'])
def status(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = 'complete'
    order.save()
    return Response({'message': 'Это GET-запрос'})


@api_view(['GET', 'POST'])
def reject(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = 'rejected'
    order.save()
    return Response({'message': 'Это GET-запрос'})
